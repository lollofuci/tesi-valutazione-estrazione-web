"""Metriche lessicali per confrontare il testo estratto dal parser con il Gold Standard.

Tutte le funzioni ricevono (parsed_text, gold_text), applicano la stessa normalizzazione
della metrica obbligatoria (rimozione del Markdown) e restituiscono valori in [0, 1].

- token_f1: la metrica del progetto base (insiemi di token: ignora ordine e ripetizioni)
- rouge_l:  basata sulla Longest Common Subsequence di parole: tiene conto dell'ordine
- chrf:     F-score su n-grammi di caratteri (n = 1..6): robusta a flessioni e accenti
- meteor:   allineamento di parole (esatto + radice) con penalita' di frammentazione

ROUGE-L, chrF e METEOR sono implementate qui invece che con le librerie standard perche':
- la tokenizzazione di `rouge-score` elimina i caratteri non ASCII (città -> citt);
- le implementazioni di riferimento sono quadratiche e troppo lente su pagine di
  decine di migliaia di parole (es. Wikipedia), mentre qui il costo e' quasi lineare.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache

from evaluation.evaluator import token_level_eval
from evaluation.advanced.text_utils import normalize_text, word_tokens


def _prf(matches: int, n_parsed: int, n_gold: int, beta: float = 1.0) -> dict[str, float]:
    precision = matches / n_parsed if n_parsed else 0.0
    recall = matches / n_gold if n_gold else 0.0
    b2 = beta * beta
    denom = b2 * precision + recall
    f = (1 + b2) * precision * recall / denom if denom > 0 else 0.0
    return {"precision": precision, "recall": recall, "f": f}


# ---------------------------------------------------------------------------
# Token F1 (metrica del progetto base)
# ---------------------------------------------------------------------------

def token_f1(parsed_text: str, gold_text: str) -> dict[str, float]:
    m = token_level_eval(parsed_text, gold_text)
    return {"precision": m["precision"], "recall": m["recall"], "f": m["f1"]}


# ---------------------------------------------------------------------------
# ROUGE-L
# ---------------------------------------------------------------------------

def lcs_length(a: list, b: list) -> int:
    """Lunghezza della Longest Common Subsequence con l'algoritmo bit-parallelo
    (Allison-Dix / Hyyro): O(len(a) * len(b) / w) usando gli interi di Python come
    vettori di bit, invece della programmazione dinamica O(len(a) * len(b)).
    """
    if not a or not b:
        return 0
    m = len(b)
    mask = (1 << m) - 1
    # match_masks[x] ha il bit j acceso se b[j] == x
    match_masks: dict = defaultdict(int)
    for j, token in enumerate(b):
        match_masks[token] |= 1 << j
    v = mask
    for token in a:
        u = v & match_masks.get(token, 0)
        v = ((v + u) | (v - u)) & mask
    return m - bin(v).count("1")


def rouge_l(parsed_text: str, gold_text: str) -> dict[str, float]:
    parsed = word_tokens(normalize_text(parsed_text))
    gold = word_tokens(normalize_text(gold_text))
    # la sequenza piu' corta fa da vettore di bit: meno memoria, stesso risultato
    lcs = lcs_length(parsed, gold) if len(parsed) >= len(gold) else lcs_length(gold, parsed)
    return _prf(lcs, len(parsed), len(gold))


# ---------------------------------------------------------------------------
# chrF (Popović, 2015), stessa definizione di sacrebleu: ordine 6, beta = 2
# ---------------------------------------------------------------------------

def _char_ngrams(text: str, n: int) -> Counter:
    return Counter(text[i:i + n] for i in range(len(text) - n + 1))


def chrf(parsed_text: str, gold_text: str, max_order: int = 6, beta: float = 2.0) -> dict[str, float]:
    # come in sacrebleu, gli spazi vengono rimossi prima di estrarre gli n-grammi
    parsed = "".join(normalize_text(parsed_text).split())
    gold = "".join(normalize_text(gold_text).split())
    p_sum = r_sum = 0.0
    orders = 0
    for n in range(1, max_order + 1):
        hyp, ref = _char_ngrams(parsed, n), _char_ngrams(gold, n)
        n_hyp, n_ref = sum(hyp.values()), sum(ref.values())
        if n_hyp == 0 or n_ref == 0:
            continue
        matches = sum((hyp & ref).values())
        p_sum += matches / n_hyp
        r_sum += matches / n_ref
        orders += 1
    if orders == 0:
        return {"precision": 0.0, "recall": 0.0, "f": 0.0}
    # come Popović (2015) e sacrebleu: prima la media di precision e recall
    # sui 6 ordini, poi una sola F-beta
    precision = p_sum / orders
    recall = r_sum / orders
    b2 = beta * beta
    denom = b2 * precision + recall
    f = (1 + b2) * precision * recall / denom if denom > 0 else 0.0
    return {"precision": precision, "recall": recall, "f": f}


# ---------------------------------------------------------------------------
# METEOR (Banerjee & Lavie, 2005), stadi "exact" e "stem"
# ---------------------------------------------------------------------------

@lru_cache(maxsize=4)
def _stemmer(lang: str):
    """Stemmer Snowball di NLTK (non richiede download); identita' se NLTK manca."""
    try:
        from nltk.stem.snowball import SnowballStemmer
    except ImportError:  # pragma: no cover - solo in ambienti senza NLTK
        return lambda w: w
    stemmer = SnowballStemmer("italian" if lang == "it" else "english")
    return lru_cache(maxsize=200_000)(stemmer.stem)


def _align(hyp: list[tuple[int, str]], ref: list[tuple[int, str]]):
    """Allineamento identico a nltk.translate.meteor_score._match_enums, ma lineare:
    scorrendo l'ipotesi dall'ultima parola, ognuna si abbina all'occorrenza ancora libera
    con indice piu' alto nel riferimento.
    """
    free_positions: dict[str, list[int]] = defaultdict(list)
    for idx, word in ref:
        free_positions[word].append(idx)
    matches = []
    used_ref = set()
    hyp_left = []
    for idx, word in reversed(hyp):
        positions = free_positions.get(word)
        if positions:
            j = positions.pop()
            matches.append((idx, j))
            used_ref.add(j)
        else:
            hyp_left.append((idx, word))
    hyp_left.reverse()
    ref_left = [(idx, word) for idx, word in ref if idx not in used_ref]
    return matches, hyp_left, ref_left


def _count_chunks(matches: list[tuple[int, int]]) -> int:
    chunks = 1
    for (h1, r1), (h2, r2) in zip(matches, matches[1:]):
        if not (h2 == h1 + 1 and r2 == r1 + 1):
            chunks += 1
    return chunks


def meteor(parsed_text: str, gold_text: str, lang: str = "it",
           alpha: float = 0.9, beta: float = 3.0, gamma: float = 0.5) -> dict[str, float]:
    hyp = word_tokens(normalize_text(parsed_text))
    ref = word_tokens(normalize_text(gold_text))
    if not hyp or not ref:
        return {"precision": 0.0, "recall": 0.0, "f": 0.0, "penalty": 0.0}

    exact, hyp_left, ref_left = _align(list(enumerate(hyp)), list(enumerate(ref)))
    stem = _stemmer(lang)
    stemmed, _, _ = _align([(i, stem(w)) for i, w in hyp_left], [(j, stem(w)) for j, w in ref_left])
    matches = sorted(exact + stemmed)

    if not matches:
        return {"precision": 0.0, "recall": 0.0, "f": 0.0, "penalty": 0.0}
    precision = len(matches) / len(hyp)
    recall = len(matches) / len(ref)
    fmean = precision * recall / (alpha * precision + (1 - alpha) * recall)
    penalty = gamma * (_count_chunks(matches) / len(matches)) ** beta
    return {"precision": precision, "recall": recall, "f": (1 - penalty) * fmean, "penalty": penalty}


# ---------------------------------------------------------------------------
# Tutte le metriche lessicali insieme
# ---------------------------------------------------------------------------

def lexical_metrics(parsed_text: str, gold_text: str, lang: str = "it") -> dict[str, float]:
    """Dizionario piatto con P/R/F di ogni metrica, es. {'rougeL_f': 0.91, ...}."""
    out: dict[str, float] = {}
    for name, result in (
        ("token", token_f1(parsed_text, gold_text)),
        ("rougeL", rouge_l(parsed_text, gold_text)),
        ("chrf", chrf(parsed_text, gold_text)),
        ("meteor", meteor(parsed_text, gold_text, lang=lang)),
    ):
        for key, value in result.items():
            out[f"{name}_{key}"] = value
    return out
