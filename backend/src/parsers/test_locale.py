import re

# Legge il markdown già salvato — zero richieste al sito
with open("output_markdown.txt", "r") as f:
    md = f.read()

def estrai_titolo(md):
    m = re.search(r'^# (.+)$', md, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return ""

def pulisci_markdown(md):
    match_inizio = re.search(r'^## [A-Z].{20,}', md, re.MULTILINE)
    if not match_inizio:
        return md.strip()
    md = md[match_inizio.start():]

    match_fine = re.search(r'\nRelated\n', md)
    if match_fine:
        md = md[:match_fine.start()]

    sostituzioni = [
        (r'(?m)^#{1,6}\s+', ''),
        (r'\[([^\]]+)\]\(https?://[^\)]+\)', r'\1'),
        (r'!\[[^\]]*\]\([^\)]*\)', ''),
        (r'https?://\S+', ''),
        (r'(?m)source:\s*[^\n]*', ''),
        (r'(?m)^.*Highcharts.*$', ''),
        (r'(?m)^.*Loading\.\.\..*$', ''),
        (r'(?m)^.*Export API.*$', ''),
        (r'(?m)^\s*OK\s*$', ''),
        (r'(?m)^\s*\|?\s*World Bank[^\n]*$', ''),
        (r'(?m)^[\s\d]+Y[\s\d]*Y.*$', ''),
        (r'(?m)^Compare:.*$', ''),
        (r'(?m)^Italy GDP\s*$', ''),
        (r'(?m)^USD Billion\s*$', ''),
    ]

    for pattern, repl in sostituzioni:
        md = re.sub(pattern, repl, md, flags=re.MULTILINE)

    linee_pulite = []
    for riga in md.splitlines():
        s = riga.strip()
        if not s:
            continue
        if s.startswith('|') and len(s) > 5:
            linee_pulite.append(riga.strip())
            continue
        if len(s) < 20 and not re.search(r'\d', s):
            continue
        if re.match(r'^[\d\s\.\,KMB\|\-]+$', s):
            continue
        linee_pulite.append(riga)

    md = '\n'.join(linee_pulite)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]{2,}', ' ', md)
    return md.strip()

# Esegui e salva il risultato
titolo = estrai_titolo(md)
parsed = pulisci_markdown(md)

print(f"TITOLO: {titolo}")
print(f"Lunghezza parsed text: {len(parsed)} caratteri")
print("\n=== PARSED TEXT ===")
print(parsed)

# Salva su file per confronto visivo
with open("output_parsed.txt", "w") as f:
    f.write(f"TITOLO: {titolo}\n\n")
    f.write(parsed)
print("\nSalvato in output_parsed.txt")