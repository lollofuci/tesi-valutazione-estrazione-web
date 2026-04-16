import re
import asyncio
from pathlib import Path
from urllib.parse import urlparse, unquote

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig


async def estrai_markdown(url: str) -> str:
    async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
        result = await crawler.arun(url=url, config=CrawlerRunConfig())
    if not result.success:
        raise RuntimeError("Errore crawl")
    return result.markdown


def estrai_titolo_da_url(url: str) -> str:
    slug = urlparse(url).path.split("/wiki/")[-1]
    return unquote(slug).replace("_", " ").strip()


def taglia_dal_titolo(md: str, titolo: str) -> str:
    m = re.search(rf"(?m)^#\s+{re.escape(titolo)}\s*$", md)
    return md[m.start():] if m else md


def taglia_fino_a_definizione(md: str, titolo: str) -> str:
    m_title = re.search(rf"(?m)^#\s+{re.escape(titolo)}\s*$", md)
    m_def = re.search(rf"(?m)^\*\*{re.escape(titolo)}\*\*", md)
    if m_title and m_def:
        return md[m_title.start():m_title.end()] + "\n\n" + md[m_def.start():]
    return md


def rimuovi_caption(md: str) -> str:
    out = []

    for line in md.splitlines():
        s = line.strip()

        if not s:
            out.append(line)
            continue

        if s.startswith("#"):
            out.append(line)
            continue

        # caption tipiche: brevi, con punto finale
        if len(s) < 40 and s.endswith("."):
            continue

        # caption spesso brevi e senza veri verbi
        if not re.search(r"\b(è|sono|fu|era|situata|costituisce|presenta|raggiunge|si trova)\b", s):
            if len(s) < 80 and s.endswith("."):
                continue

        out.append(line)

    return "\n".join(out)


def pulisci_markdown(md: str, url: str) -> str:
    titolo = estrai_titolo_da_url(url)

    md = taglia_dal_titolo(md, titolo)
    md = taglia_fino_a_definizione(md, titolo)
    md = re.sub(r"\r\n?", "\n", md)

    # Link markdown / wikilink -> conserva il testo
    sostituzioni = [
        (r"\[([^\]]+)\]\([^)]+\)", r"\1"),          # [testo](url) -> testo
        (r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1"),     # [[voce|testo]] -> testo
        (r"\[\[(\d+)\]\]", r""),                   # [[1]] -> ""
        (r"\[\[([^\]]+)\]\]", r"\1"),              # [[testo]] -> testo
        (r"\(https?://[^)]*\)", r""),              # URL residui
        (r'\s*"[^"\n]*\\\([^"\n]*\\\)"\)', r""),   # residui tipo "Comune \(Italia\)")
    ]
    for pattern, repl in sostituzioni:
        md = re.sub(pattern, repl, md)

    # Righe inutili tipiche di Wikipedia
    patterns_lineari = [
        r"(?m)^\[modifica \| modifica wikitesto\]\n?",
        r"(?m)^Modifica collegamenti\n?",
        r"(?m)^Coordinate:.*\n?",
        r"(?m)^Da Wikipedia, l'enciclopedia libera\.\n?",
        r"(?mi)^.*disambigua.*\n?",
        r"(?mi)^\s*Lo stesso argomento in dettaglio:.*\n?",
        r"(?mi)^Niente fonti.*\n?",
        r"(?m)^\[Niente fonti\]\n?",
        r"(?m)^\*\*Questa voce.*\n?",
        r"(?m)^\*\*Commento\*\*.*\n?",
        r"(?m)^Puoi migliorare questa voce.*\n?",
        r"(?mi)^aggiungendo citazioni.*\n?",
        r"(?m)^\* \* \*\n?",
        r"(?m)^comune .*$\n?",
        r"(?m)^.*\|\s*$\n?",
        r"(?m)^sismica:.*\n?",
        r"(?m)^climatica:.*\n?",
        r"(?m)^\(https?://it\.wikipedia\.org/wiki/File:.*\n?",
        r"(?m)^!\s*",
        r"!\s*",
        r"(?m)^[A-Za-z0-9._-]*\.(jpg|jpeg|png|svg|webp)\).*",
    ]
    for pattern in patterns_lineari:
        md = re.sub(pattern, "", md, flags=re.IGNORECASE if "jpg|jpeg|png|svg|webp" in pattern else 0)

    # Pulizia incipit AFI / ascolta
    md = re.sub(r"\bAFI:\s*", "", md)
    md = re.sub(r"ascoltaⓘ", "", md)

    # Caption immagini
    md = rimuovi_caption(md)

    # Taglia da Note in poi
    md = re.sub(
        r"(?ms)^##\s+(Note|Bibliografia|Voci correlate|Altri progetti|Collegamenti esterni|Categorie nascoste)\s*$.*",
        "",
        md,
    )

    # Cleanup finale
    md = re.sub(r"\[\s*\]", "", md)
    md = re.sub(r"[ \t]+", " ", md)
    md = re.sub(r"\n{3,}", "\n\n", md)

    return md.strip()


async def main():
    url = "https://it.wikipedia.org/wiki/Avellino"

    grezzo = await estrai_markdown(url)
    pulito = pulisci_markdown(grezzo, url)

    Path("grezzo.txt").write_text(grezzo, encoding="utf-8")
    Path("testo.txt").write_text(pulito, encoding="utf-8")

    print("Creati grezzo.txt e testo.txt")
    print("\n=== PRIMI 8000 CARATTERI ===\n")
    print(pulito[:8000])


if __name__ == "__main__":
    asyncio.run(main())