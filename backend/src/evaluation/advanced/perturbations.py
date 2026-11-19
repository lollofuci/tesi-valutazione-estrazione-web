"""Degradazioni controllate del Gold Standard per la meta-valutazione delle metriche.

Idea: il Gold Standard e' per definizione un'estrazione perfetta. Rovinandolo in modo
controllato si ottengono testi di qualita' NOTA, senza bisogno di annotazioni manuali:
una buona metrica deve dare punteggi piu' bassi al crescere della gravita' (severity).

Ogni tipo simula un errore tipico di un parser reale:
- truncate:        il parser si ferma troppo presto (contenuto finale perso)
- drop_lines:      il parser salta blocchi sparsi (paragrafi, righe di tabelle)
- add_boilerplate: il parser include menu, footer, banner (presi dall'HTML della pagina)
- shuffle:         il parser restituisce i blocchi in ordine sbagliato
- corrupt_numbers: valori numerici alterati (es. dati presi da una versione diversa della pagina)

La severity s e' sempre "la frazione del testo che e' sbagliata":
- truncate e drop_lines rimuovono una frazione s del contenuto;
- add_boilerplate fa si' che il rumore sia una frazione s del testo risultante;
- shuffle sposta una frazione s delle righe;
- corrupt_numbers altera una frazione s dei numeri.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass

from evaluation.advanced.text_utils import html_visible_text, split_units

PERTURBATION_TYPES = ["truncate", "drop_lines", "add_boilerplate", "shuffle", "corrupt_numbers"]
DEFAULT_SEVERITIES = [0.25, 0.5, 0.75]

_NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")

# Usato solo se nella pagina non c'e' abbastanza testo di contorno.
_FALLBACK_BOILERPLATE = [
    "Accetta tutti i cookie", "Privacy Policy", "Termini di servizio", "Iscriviti alla newsletter",
    "Seguici su Facebook", "Home", "Contatti", "Pubblicità", "Accedi", "Cerca",
    "© Tutti i diritti riservati", "Scarica l'app",
]


@dataclass
class Variant:
    ptype: str
    severity: float            # severity richiesta
    text: str
    effective_severity: float  # severity effettivamente ottenuta (vedi effective_severity)


def _rng(seed_key: str) -> random.Random:
    return random.Random(seed_key)


def truncate(gold: str, s: float, **_) -> str:
    keep = int(len(gold) * (1 - s))
    cut = gold[:keep]
    space = max(cut.rfind(" "), cut.rfind("\n"))
    return cut[:space] if space > 0 else cut


def drop_lines(gold: str, s: float, rng: random.Random, **_) -> str:
    """Elimina righe scelte a caso finche' non e' stata rimossa una frazione s dei caratteri."""
    lines = split_units(gold)
    if len(lines) <= 1:
        return truncate(gold, s)  # un testo di una riga non si puo' "bucare": si tronca
    total = sum(len(line) for line in lines)
    order = list(range(len(lines)))
    rng.shuffle(order)
    dropped, removed = set(), 0
    for i in order:
        if removed >= s * total or len(dropped) == len(lines) - 1:
            break
        dropped.add(i)
        removed += len(lines[i])
    return "\n".join(line for i, line in enumerate(lines) if i not in dropped)


def _boilerplate_lines(gold: str, html: str) -> list[str]:
    """Righe visibili della pagina che NON fanno parte del Gold Standard."""
    gold_lines = set(split_units(gold))
    gold_lower = gold.lower()
    noise = []
    for line in split_units(html_visible_text(html)):
        if line in gold_lines or line.lower() in gold_lower:
            continue
        noise.append(line)
    return noise or list(_FALLBACK_BOILERPLATE)


def add_boilerplate(gold: str, s: float, rng: random.Random, html: str = "", **_) -> str:
    """Aggiunge righe di contorno della pagina finche' il rumore e' una frazione s del totale.

    Le righe non vengono ripetute: se la pagina non ha abbastanza testo di contorno la
    severity effettiva resta piu' bassa (viene misurata da effective_severity).
    """
    if s <= 0:
        return gold
    target = int(len(gold) * s / (1 - s))
    pool = _boilerplate_lines(gold, html)
    noise: list[str] = []
    size = 0
    for line in pool:
        if size >= target:
            break
        noise.append(line)
        size += len(line) + 1
    half = len(noise) // 2
    # come nelle pagine reali: meta' in testa (menu, header), meta' in coda (footer)
    return "\n".join(noise[:half] + [gold] + noise[half:])


def shuffle(gold: str, s: float, rng: random.Random, **_) -> str:
    lines = split_units(gold)
    k = round(len(lines) * s)
    if k < 2:
        return gold
    positions = sorted(rng.sample(range(len(lines)), k))
    moved = [lines[p] for p in positions]
    original = list(moved)
    for _ in range(10):          # evita, se possibile, la permutazione identica
        rng.shuffle(moved)
        if moved != original:
            break
    out = list(lines)
    for p, line in zip(positions, moved):
        out[p] = line
    return "\n".join(out)


def _alter_number(token: str, rng: random.Random) -> str:
    digits = [i for i, ch in enumerate(token) if ch.isdigit()]
    chars = list(token)
    i = rng.choice(digits)
    chars[i] = rng.choice([d for d in "0123456789" if d != chars[i]])
    return "".join(chars)


def corrupt_numbers(gold: str, s: float, rng: random.Random, **_) -> str:
    matches = list(_NUMBER_RE.finditer(gold))
    k = round(len(matches) * s)
    if k == 0:
        return gold
    chosen = set(rng.sample(range(len(matches)), k))
    out, last = [], 0
    for i, m in enumerate(matches):
        out.append(gold[last:m.start()])
        out.append(_alter_number(m.group(0), rng) if i in chosen else m.group(0))
        last = m.end()
    out.append(gold[last:])
    return "".join(out)


_FUNCTIONS = {
    "truncate": truncate,
    "drop_lines": drop_lines,
    "add_boilerplate": add_boilerplate,
    "shuffle": shuffle,
    "corrupt_numbers": corrupt_numbers,
}


def perturb(gold: str, ptype: str, severity: float, html: str = "", seed: str = "") -> str:
    """Applica una perturbazione; con lo stesso seed il risultato e' riproducibile."""
    rng = _rng(f"{seed}|{ptype}|{severity}")
    return _FUNCTIONS[ptype](gold, severity, rng=rng, html=html)


def effective_severity(gold: str, text: str, ptype: str, severity: float) -> float:
    """Frazione di testo effettivamente "sbagliata" nella variante.

    Per troncamento, righe eliminate e rumore aggiunto si misura sui caratteri; per
    shuffle e numeri alterati coincide con la severity richiesta.
    """
    if ptype in ("truncate", "drop_lines"):
        return 1 - len(text) / len(gold) if gold else 0.0
    if ptype == "add_boilerplate":
        return 1 - len(gold) / len(text) if text else 0.0
    return severity


def generate_variants(gold: str, html: str = "", seed: str = "",
                      types: list[str] | None = None,
                      severities: list[float] | None = None) -> list[Variant]:
    """Tutte le varianti di un documento: tipo x severity (piu' la copia intatta, s = 0)."""
    variants = [Variant("none", 0.0, gold, 0.0)]
    for ptype in types or PERTURBATION_TYPES:
        for s in severities or DEFAULT_SEVERITIES:
            text = perturb(gold, ptype, s, html=html, seed=seed)
            eff = round(effective_severity(gold, text, ptype, s), 4)
            variants.append(Variant(ptype, s, text, eff))
    return variants
