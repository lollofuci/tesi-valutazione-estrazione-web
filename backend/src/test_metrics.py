"""Test di correttezza delle metriche reimplementate in evaluation/advanced/metrics.py.

ROUGE-L, chrF e METEOR sono state riscritte (per gestire accenti e testi lunghi),
quindi qui le confrontiamo con le implementazioni di riferimento su testi brevi:
- lcs_length (bit-parallela)  -> programmazione dinamica classica
- chrf                        -> sacrebleu (CHRF con i parametri di default)
- meteor                      -> NLTK (single_meteor_score, senza sinonimi WordNet)
- LongBertScorer (BERTScore)  -> libreria bert-score (stesso modello e strato, senza idf
                                 e senza rescaling), su testi sotto i 510 token

Uso (dalla cartella backend/src, con il venv attivo):
    pip install pytest sacrebleu
    python -m pytest test_metrics.py -v

Il test di BERTScore richiede anche la libreria bert-score e il modello BERT (~700 MB):
se bert-score non è installata viene saltato. Dalla cartella del progetto, nel container
del backend (il codice viene montato dalla cartella, come in esperimenti.sh):
    docker compose run --rm --no-deps -v "$PWD/backend/src:/app/src" backend sh -c \
        "pip install bert-score pytest sacrebleu && python -m pytest test_metrics.py -v -s"
"""

import random

import pytest

from evaluation.advanced.metrics import chrf, lcs_length, meteor, rouge_l, token_f1
from evaluation.advanced.text_utils import normalize_text, word_tokens

# Vocabolario piccolo, con parole flesse (gatto/gatti, mangia/mangiare...),
# così nei testi casuali ci sono molte ripetizioni e molti abbinamenti per radice.
VOCAB_IT = ["il", "la", "gatto", "gatti", "mangia", "mangiare", "mangiato", "topo", "topi",
            "casa", "case", "città", "perché", "di", "e", "rosso", "rossa", "23", "2026"]
VOCAB_EN = ["the", "cat", "cats", "eats", "eating", "eaten", "mouse", "house", "houses",
            "red", "and", "of", "playing", "played", "player", "23", "2026"]

N_CASI = 300


def frase_casuale(rng: random.Random, vocab: list[str], max_len: int = 30) -> str:
    return " ".join(rng.choice(vocab) for _ in range(rng.randint(1, max_len)))


# ---------------------------------------------------------------------------
# Esempio della tesi: stesse parole, ordine diverso
# ---------------------------------------------------------------------------

GS = "il gatto mangia il topo"
ESTRATTO = "il topo mangia il gatto"


def test_esempio_token_f1_cieca_all_ordine():
    assert token_f1(ESTRATTO, GS)["f"] == pytest.approx(1.0)


def test_esempio_rouge_l():
    # LCS = "il mangia il" -> 3 parole su 5
    assert rouge_l(ESTRATTO, GS)["f"] == pytest.approx(0.6)


def test_esempio_meteor():
    # 5 parole abbinate in 4 chunk: penalità = 0,5 * (4/5)^3 = 0,256
    assert meteor(ESTRATTO, GS, lang="it")["f"] == pytest.approx(1 - 0.256)


def test_testi_identici_valgono_1():
    testo = "Roma è la capitale d'Italia. La città conta 2,7 milioni di abitanti."
    assert rouge_l(testo, testo)["f"] == pytest.approx(1.0)
    assert chrf(testo, testo)["f"] == pytest.approx(1.0)
    # METEOR non arriva mai esattamente a 1: anche con un solo chunk resta
    # una penalità minima di 0,5 * (1 / numero di parole)^3
    n = len(word_tokens(testo))
    assert meteor(testo, testo, lang="it")["f"] == pytest.approx(1.0 - 0.5 * (1 / n) ** 3)


def test_testo_vuoto_vale_0():
    for metrica in (rouge_l, chrf, meteor):
        assert metrica("", GS)["f"] == 0.0
        assert metrica(GS, "")["f"] == 0.0


# ---------------------------------------------------------------------------
# ROUGE-L: algoritmo bit-parallelo contro programmazione dinamica
# ---------------------------------------------------------------------------

def lcs_programmazione_dinamica(a: list, b: list) -> int:
    """Versione da manuale: tabella (len(a)+1) x (len(b)+1)."""
    L = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[len(a)][len(b)]


def test_lcs_bit_parallela_uguale_a_programmazione_dinamica():
    rng = random.Random(42)
    for _ in range(N_CASI):
        a = rng.choices(VOCAB_IT, k=rng.randint(0, 60))
        b = rng.choices(VOCAB_IT, k=rng.randint(0, 60))
        assert lcs_length(a, b) == lcs_programmazione_dinamica(a, b), (a, b)


# ---------------------------------------------------------------------------
# chrF contro sacrebleu
# ---------------------------------------------------------------------------

def test_chrf_uguale_a_sacrebleu():
    from sacrebleu.metrics import CHRF

    riferimento = CHRF()  # ordine 6 sui caratteri, nessun n-gramma di parole, beta = 2
    rng = random.Random(7)
    for _ in range(N_CASI):
        vocab = rng.choice([VOCAB_IT, VOCAB_EN])
        hyp, ref = frase_casuale(rng, vocab), frase_casuale(rng, vocab)
        atteso = riferimento.sentence_score(normalize_text(hyp), [normalize_text(ref)]).score / 100
        assert chrf(hyp, ref)["f"] == pytest.approx(atteso, abs=1e-9), (hyp, ref)


# ---------------------------------------------------------------------------
# METEOR contro NLTK
# ---------------------------------------------------------------------------

class SenzaSinonimi:
    """Sostituto di WordNet che non trova mai sinonimi: la nostra METEOR non usa
    il terzo stadio (WordNet esiste solo per l'inglese)."""

    def synsets(self, word):
        return []


def test_meteor_uguale_a_nltk():
    from nltk.stem.snowball import SnowballStemmer
    from nltk.translate.meteor_score import single_meteor_score

    rng = random.Random(123)
    for _ in range(N_CASI):
        lang = rng.choice(["it", "en"])
        vocab = VOCAB_IT if lang == "it" else VOCAB_EN
        hyp, ref = frase_casuale(rng, vocab), frase_casuale(rng, vocab)
        atteso = single_meteor_score(
            word_tokens(normalize_text(ref)),
            word_tokens(normalize_text(hyp)),
            stemmer=SnowballStemmer("italian" if lang == "it" else "english"),
            wordnet=SenzaSinonimi(),
        )
        assert meteor(hyp, ref, lang=lang)["f"] == pytest.approx(atteso, abs=1e-9), (lang, hyp, ref)


# ---------------------------------------------------------------------------
# BERTScore contro la libreria bert-score
# ---------------------------------------------------------------------------
# La libreria tronca i testi a 512 token, la nostra versione li divide in blocchi da 510:
# il confronto ha senso solo su testi brevi, dove i due metodi devono coincidere.

COPPIE_BERTSCORE = [
    # (testo estratto, testo di riferimento)
    ("il gatto mangia il topo", "il gatto mangia il topo"),
    ("il topo mangia il gatto", "il gatto mangia il topo"),
    ("Roma è la capitale d'Italia.", "La capitale d'Italia è Roma."),
    ("La città conta 2,7 milioni di abitanti.", "La città conta 2,8 milioni di abitanti."),
    ("Il quark è una particella elementare.", "Il quark è una particella elementare e un costituente della materia."),
    ("Home Notizie Accedi Il quark è una particella elementare. Cookie Privacy",
     "Il quark è una particella elementare."),
    ("Oggi a Roma: sereno, massima 21 °C, minima 12 °C.", "Roma, oggi: cielo sereno con massima di 21 °C e minima di 12 °C."),
    ("Previsioni orarie: 10:00 18 °C, 11:00 19 °C, 12:00 20 °C", "Previsioni orarie: 12:00 20 °C, 11:00 19 °C, 10:00 18 °C"),
    ("Perché la città è più grande?", "Perché la città è così grande?"),
    ("The Gross Domestic Product (GDP) in Italy was worth 2,254 billion US dollars in 2023.",
     "The GDP in Italy was worth 2,254 billion US dollars in 2023."),
    ("Crude Oil fell to 71.2 USD/Bbl.", "Crude oil rose to 73.5 USD/Bbl."),
    ("Sinner beats Alcaraz in the final.", "Alcaraz beats Sinner in the final."),
    ("Jannik Sinner, born 16 August 2001, is an Italian tennis player.",
     "Jannik Sinner (born 16 August 2001) is an Italian professional tennis player."),
    ("Head to head: 5 wins, 4 losses", "Head-to-head record: 5 wins and 4 losses"),
    ("Accept all cookies Subscribe now", "The match lasted three hours."),
    ("A", "Una frase completamente diversa dal testo estratto."),
    ("Il parser ha estratto solo il titolo.",
     "Il parser ha estratto il titolo, il primo paragrafo e la tabella dei dati."),
    ("Tabella: Italia | 2023 | 2,1% ; Francia | 2023 | 0,9%", "Italia 2023 2,1% Francia 2023 0,9%"),
    ("mangia mangiare mangiato", "mangiava mangiano mangeranno"),
    ("città perché più già", "citta perche piu gia"),
]

# Il primo run del test (6/11/2026) ha mostrato che su 13 coppie su 20 i due valori
# coincidono (differenze ~1e-7), mentre sulle altre la libreria dà un punteggio un po'
# più alto (fino a +0,034 sulle coppie più diverse). Il motivo è una differenza di
# definizione: bert-score esclude [CLS] e [SEP] dalla media (peso nullo), ma li lascia
# tra i candidati quando cerca il token più simile; LongBertScorer li esclude del tutto.
# Per verificarlo i test sono due:
#  1. una ricostruzione con le regole della libreria, che usa lo stesso modello, strato,
#     tokenizzazione e normalizzazione di LongBertScorer, deve dare gli stessi numeri;
#  2. LongBertScorer non può mai superare la libreria (cerca il massimo su meno token)
#     e la differenza resta piccola.

TOLLERANZA_BERTSCORE = 1e-5          # arrotondamenti (batch e padding diversi)
DIFFERENZA_MASSIMA_TOKEN_SPECIALI = 0.05


def bertscore_con_token_speciali(scorer, parsed_text: str, gold_text: str) -> dict[str, float]:
    """BERTScore con le regole della libreria bert-score: [CLS] e [SEP] non contano nella
    media ma possono essere scelti come token più simile. Solo per testi brevi."""
    import torch

    scorer._load()
    tok, model = scorer._tokenizer, scorer._model

    def embed(text: str):
        ids = [tok.cls_token_id] + tok(text, add_special_tokens=False)["input_ids"] + [tok.sep_token_id]
        with torch.no_grad():
            hidden = model(input_ids=torch.tensor([ids])).hidden_states[scorer.layer][0]
        return torch.nn.functional.normalize(hidden, dim=-1)

    cand, ref = embed(normalize_text(parsed_text)), embed(normalize_text(gold_text))
    sims = cand @ ref.T
    precision = sims.max(dim=1).values[1:-1].mean().item()   # righe: token veri dell'estratto
    recall = sims.max(dim=0).values[1:-1].mean().item()      # colonne: token veri del GS
    f = 2 * precision * recall / (precision + recall)
    return {"precision": precision, "recall": recall, "f": f}


@pytest.fixture(scope="module")
def bertscore_libreria():
    bert_score = pytest.importorskip("bert_score")
    from evaluation.advanced.bertscore import DEFAULT_LAYER, DEFAULT_MODEL, LongBertScorer

    libreria = bert_score.BERTScorer(model_type=DEFAULT_MODEL, num_layers=DEFAULT_LAYER,
                                     idf=False, rescale_with_baseline=False)
    candidati = [normalize_text(c) for c, _ in COPPIE_BERTSCORE]
    riferimenti = [normalize_text(r) for _, r in COPPIE_BERTSCORE]
    P, R, F = libreria.score(candidati, riferimenti)
    attesi = [{"precision": P[k].item(), "recall": R[k].item(), "f": F[k].item()}
              for k in range(len(COPPIE_BERTSCORE))]
    return LongBertScorer(), attesi


def _diff(a: dict, b: dict) -> float:
    return max(abs(a[k] - b[k]) for k in ("precision", "recall", "f"))


def test_bertscore_stesso_calcolo_della_libreria(bertscore_libreria):
    nostro, attesi = bertscore_libreria
    differenze = []
    for k, (c, r) in enumerate(COPPIE_BERTSCORE):
        d = _diff(bertscore_con_token_speciali(nostro, c, r), attesi[k])
        differenze.append(d)
        print(f"{k:2d}  con token speciali: diff max={d:.2e}")
    print(f"Differenza massima dalla libreria (stesse regole): {max(differenze):.2e}")
    assert max(differenze) <= TOLLERANZA_BERTSCORE


def test_bertscore_effetto_dei_token_speciali(bertscore_libreria):
    nostro, attesi = bertscore_libreria
    differenze = []
    for k, (c, r) in enumerate(COPPIE_BERTSCORE):
        mio = nostro.score(c, r)
        for chiave in ("precision", "recall", "f"):
            assert mio[chiave] <= attesi[k][chiave] + TOLLERANZA_BERTSCORE, (k, chiave)
        d = _diff(mio, attesi[k])
        differenze.append(d)
        print(f"{k:2d}  nostro F={mio['f']:.6f}  libreria F={attesi[k]['f']:.6f}  diff max={d:.2e}")
    uguali = sum(d <= TOLLERANZA_BERTSCORE for d in differenze)
    print(f"Coppie identiche: {uguali} su {len(differenze)}; differenza massima: {max(differenze):.2e}")
    assert max(differenze) <= DIFFERENZA_MASSIMA_TOKEN_SPECIALI
