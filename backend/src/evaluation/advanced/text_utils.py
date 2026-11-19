"""Funzioni di supporto comuni alle metriche e ai giudici."""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from evaluation.evaluator import remove_markdown

# Token "parola": sequenze di caratteri alfanumerici Unicode (mantiene accenti: città, perché).
_WORD_RE = re.compile(r"\w+", re.UNICODE)

# Poche parole funzionali molto frequenti, sufficienti a distinguere italiano e inglese.
_IT_STOPWORDS = {
    "il", "lo", "la", "i", "gli", "le", "di", "del", "della", "che", "e", "è", "un", "una",
    "per", "con", "non", "nel", "nella", "sono", "da", "dei", "delle", "al", "alla", "si",
}
_EN_STOPWORDS = {
    "the", "of", "and", "to", "in", "is", "a", "an", "that", "for", "on", "with", "as",
    "are", "was", "by", "at", "from", "it", "this", "be", "or", "has", "have", "his",
}

# Tag HTML che non contengono testo visibile all'utente.
_INVISIBLE_TAGS = ["script", "style", "noscript", "svg", "template", "iframe", "head", "meta", "link"]


def normalize_text(text: str) -> str:
    """Rimuove il Markdown (come token_level_eval) e compatta gli spazi."""
    plain = remove_markdown(text or "")
    plain = re.sub(r"[ \t]+", " ", plain)
    plain = re.sub(r"\n+", "\n", plain)
    return plain.strip()


def word_tokens(text: str) -> list[str]:
    """Lista ordinata di token in minuscolo (a differenza di token_level_eval, conserva l'ordine)."""
    return _WORD_RE.findall((text or "").lower())


def detect_language(text: str) -> str:
    """Restituisce 'it' o 'en' contando le parole funzionali più frequenti."""
    tokens = word_tokens(text[:20000])
    it_hits = sum(1 for t in tokens if t in _IT_STOPWORDS)
    en_hits = sum(1 for t in tokens if t in _EN_STOPWORDS)
    return "it" if it_hits >= en_hits else "en"


def html_visible_text(html: str) -> str:
    """Estrae tutto il testo visibile di una pagina HTML (contenuto principale + boilerplate).

    Serve al giudice senza Gold Standard: l'LLM vede la pagina "come la vedrebbe un utente"
    e deve stabilire se il testo estratto dal parser ne coglie il contenuto principale.
    """
    soup = BeautifulSoup(html or "", "html.parser")
    for tag in soup(_INVISIBLE_TAGS):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def split_units(text: str) -> list[str]:
    """Divide un testo in unità (righe non vuote), usate da perturbazioni e analisi."""
    return [line.strip() for line in (text or "").splitlines() if line.strip()]


def truncate_chars(text: str, max_chars: int) -> str:
    """Tronca a max_chars senza spezzare l'ultima parola."""
    text = text or ""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    space = cut.rfind(" ")
    return cut[:space] if space > max_chars * 0.8 else cut
