"""Analisi dei risultati: tabelle LaTeX (results/tables) e grafici (results/figures).

Funziona anche con risultati parziali (es. senza giudici o senza BERTScore): le analisi
per cui mancano i dati vengono saltate.

Uso:  python -m experiments.analyze
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from evaluation.advanced.agreement import correlation, exact_agreement, quadratic_weighted_kappa
from experiments import config
from experiments.common import read_jsonl

METRICS = {
    "token_f": "Token F1",
    "rougeL_f": "ROUGE-L",
    "chrf_f": "chrF",
    "meteor_f": "METEOR",
    "bertscore_f": "BERTScore",
}
PTYPES = {
    "truncate": "Troncamento",
    "drop_lines": "Righe eliminate",
    "add_boilerplate": "Boilerplate",
    "shuffle": "Ordine alterato",
    "corrupt_numbers": "Numeri alterati",
}
DOMAINS = {
    "it.wikipedia.org": "Wikipedia",
    "www.atptour.com": "ATP Tour",
    "www.accuweather.com": "AccuWeather",
    "tradingeconomics.com": "Trading Economics",
}
MODES = {"with_gs": "con GS", "without_gs": "senza GS"}

# Palette categoriale (ordine fisso) e colori di testo, validati per il fondo chiaro.
SERIES_COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*"]
TEXT_PRIMARY, TEXT_SECONDARY, GRID = "#0b0b0b", "#52514e", "#e4e3df"


# ---------------------------------------------------------------------------
# Caricamento
# ---------------------------------------------------------------------------

def load_frames():
    cases = pd.DataFrame(read_jsonl(config.CASES_PATH)).drop(columns=["text"], errors="ignore")
    metrics = pd.DataFrame(read_jsonl(config.METRICS_PATH))
    judges = pd.DataFrame(read_jsonl(config.JUDGES_PATH))
    if not metrics.empty:
        metrics = metrics.drop_duplicates("case_id", keep="last")
        cases = cases.merge(metrics, on="case_id", how="left")
    if not judges.empty:
        # "token repeat limit": Ollama interrompe un modello che ripete all'infinito gli stessi
        # token. E' un fallimento del giudice (come un JSON non valido), non un errore di rete.
        repeat = judges["error"].fillna("").str.contains("repeat limit")
        judges.loc[repeat, ["error", "valid_json", "score"]] = ["", False, None]
        judges = judges[judges["error"].fillna("") == ""]
        judges = judges.drop_duplicates(["case_id", "model", "mode"], keep="last")
        judges = judges.merge(cases, on="case_id", how="left")
    metric_cols = [c for c in METRICS if c in cases.columns]
    return cases, judges, metric_cols


# ---------------------------------------------------------------------------
# Tabelle LaTeX
# ---------------------------------------------------------------------------

def num(x, digits: int = 3) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "--"
    text = f"{x:.{digits}f}"
    if float(text) == 0:
        text = text.lstrip("-")  # evita "-0,00"
    return text.replace(".", ",")


def latex_table(rows: list[list[str]], header: list[str], caption: str, label: str,
                align: str | None = None, bold_last_row: bool = False) -> str:
    align = align or "l" + "c" * (len(header) - 1)
    lines = [r"\begin{table}[htbp]", r"  \centering", r"  \small",
             rf"  \begin{{tabular}}{{{align}}}", r"    \toprule",
             "    " + " & ".join(rf"\textbf{{{h}}}" for h in header) + r" \\", r"    \midrule"]
    for i, row in enumerate(rows):
        if bold_last_row and i == len(rows) - 1:
            lines.append(r"    \midrule")
            row = [rf"\textbf{{{c}}}" for c in row]
        lines.append("    " + " & ".join(row) + r" \\")
    lines += [r"    \bottomrule", r"  \end{tabular}", rf"  \caption{{{caption}}}",
              rf"  \label{{{label}}}", r"\end{table}", ""]
    return "\n".join(lines)


def save(name: str, content: str) -> None:
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)
    (config.TABLES_DIR / name).write_text(content, encoding="utf-8")
    print(f"  tabella: {config.TABLES_DIR / name}")


# ---------------------------------------------------------------------------
# A. Qualita' dei parser reali secondo ogni metrica
# ---------------------------------------------------------------------------

def table_parser_quality(cases: pd.DataFrame, metric_cols: list[str]) -> None:
    parser = cases[cases["kind"] == "parser"]
    if parser.empty or not metric_cols:
        return
    rows = []
    for domain, label in DOMAINS.items():
        sub = parser[parser["domain"] == domain]
        if not sub.empty:
            rows.append([label] + [num(sub[m].mean()) for m in metric_cols])
    rows.append(["Media"] + [num(parser[m].mean()) for m in metric_cols])
    save("parser_quality.tex", latex_table(
        rows, ["Dominio"] + [METRICS[m] for m in metric_cols],
        "Qualità dei parser secondo ciascuna metrica (F-score medio per dominio, modalità offline).",
        "tab:parser-quality", bold_last_row=True))


# ---------------------------------------------------------------------------
# B. Meta-valutazione: sensibilita' delle metriche alle perturbazioni
# ---------------------------------------------------------------------------

def sensitivity(df: pd.DataFrame, score_col: str, ptype: str) -> float:
    """-Spearman(severity effettiva, punteggio) su: GS intatto + perturbazioni del tipo.
    1 = il punteggio scende sempre al crescere dell'errore; 0 = la metrica non se ne accorge."""
    sub = df[(df["kind"] == "perturbation") & (df["ptype"].isin(["none", ptype]))]
    r = correlation(sub["effective_severity"], sub[score_col], "spearman")["r"]
    return -r if not math.isnan(r) else float("nan")


def bootstrap_by_document(df: pd.DataFrame, statistic, n_boot: int = 1000,
                          alpha: float = 0.05, seed: int = 42) -> tuple[float, float]:
    """Intervallo di confidenza bootstrap (percentile, 95%) di una statistica.

    Si ricampionano i DOCUMENTI, non i singoli casi: i 17 casi di uno stesso documento
    derivano dallo stesso Gold Standard e non sono indipendenti tra loro. Ricampionare
    i casi darebbe intervalli troppo stretti, cioè una precisione che i dati non hanno.
    """
    groups = {doc: sub for doc, sub in df.groupby("doc_id")}
    docs = list(groups)
    if len(docs) < 2:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(n_boot):
        sample = rng.choice(docs, size=len(docs), replace=True)
        value = statistic(pd.concat([groups[d] for d in sample], ignore_index=True))
        if not math.isnan(value):
            values.append(value)
    if not values:
        return float("nan"), float("nan")
    return float(np.percentile(values, 100 * alpha / 2)), float(np.percentile(values, 100 * (1 - alpha / 2)))


def num_ci(value: float, ci: tuple[float, float]) -> str:
    """Valore con intervallo di confidenza, es. 0,92 [0,88; 0,95]."""
    return f"{num(value, 2)} [{num(ci[0], 2)}; {num(ci[1], 2)}]"


def table_sensitivity(cases: pd.DataFrame, metric_cols: list[str]) -> pd.DataFrame | None:
    if not metric_cols:
        return None
    data = {m: {p: sensitivity(cases, m, p) for p in PTYPES} for m in metric_cols}
    frame = pd.DataFrame(data).T
    frame["media"] = frame.mean(axis=1)
    rows = [[METRICS[m]] + [num(frame.loc[m, p], 2) for p in PTYPES] + [num(frame.loc[m, "media"], 2)]
            for m in metric_cols]
    save("sensitivity.tex", latex_table(
        rows, ["Metrica"] + list(PTYPES.values()) + ["Media"],
        "Sensibilità delle metriche alle perturbazioni controllate: opposto della correlazione di "
        "Spearman tra gravità dell'errore e punteggio (1 = la metrica penalizza sempre "
        "l'errore, 0 = non lo rileva).", "tab:sensitivity", align="l" + "c" * (len(PTYPES) + 1)))

    # stessa tabella con gli intervalli di confidenza (più larga: per l'appendice o il testo)
    rows_ci = []
    for m in metric_cols:
        row = [METRICS[m]]
        for p in PTYPES:
            ci = bootstrap_by_document(cases, lambda d, m=m, p=p: sensitivity(d, m, p))
            row.append(num_ci(frame.loc[m, p], ci))
        rows_ci.append(row)
    save("sensitivity_ci.tex", latex_table(
        rows_ci, ["Metrica"] + list(PTYPES.values()),
        "Sensibilità delle metriche con intervallo di confidenza al 95\\% (bootstrap sui "
        "20 documenti, 1000 ricampionamenti).", "tab:sensitivity-ci",
        align="l" + "c" * len(PTYPES)))
    return frame


# ---------------------------------------------------------------------------
# C. Giudici LLM
# ---------------------------------------------------------------------------

def table_judges(judges: pd.DataFrame) -> pd.DataFrame | None:
    if judges.empty:
        return None
    rows, records = [], []
    for (model, mode), sub in judges.groupby(["model", "mode"], sort=False):
        valid = sub[sub["valid_json"]]
        pert = valid[valid["kind"] == "perturbation"]
        intact = pert[pert["ptype"] == "none"]["score"].mean()
        damaged = pert[pert["ptype"] != "none"]["score"].mean()
        sens = correlation(pert["effective_severity"], pert["score"], "spearman")["r"]
        rec = {"model": model, "mode": mode,
               "valid": sub["valid_json"].mean(), "latency": sub["latency_s"].median(),
               "intact": intact, "damaged": damaged, "gap": intact - damaged,
               "sensitivity": -sens if not math.isnan(sens) else float("nan")}
        records.append(rec)
        rows.append([model, MODES.get(mode, mode), num(100 * rec["valid"], 0) + r"\%",
                     num(rec["latency"], 1), num(intact, 2), num(damaged, 2), num(rec["gap"], 2),
                     num(rec["sensitivity"], 2)])
    save("judges.tex", latex_table(
        rows, ["Modello", "Modalità", "JSON valido", "Latenza (s)", "GS intatto", "GS degradato",
               "Differenza", "Sensibilità"],
        "Confronto tra giudici LLM: validità del JSON, latenza mediana, punteggio medio sul "
        "Gold Standard intatto e degradato (severità 0,5) e sensibilità alla gravità dell'errore.",
        "tab:judges", align="llcccccc"))
    return pd.DataFrame(records)


def table_judge_agreement(judges: pd.DataFrame) -> None:
    """Accordo tra la modalita' con GS e quella senza GS dello stesso modello."""
    if judges.empty or judges["mode"].nunique() < 2:
        return
    rows = []
    for model, sub in judges[judges["valid_json"]].groupby("model", sort=False):
        pivot = sub.pivot_table(index="case_id", columns="mode", values="score")
        if {"with_gs", "without_gs"} <= set(pivot.columns):
            pivot = pivot.dropna()
            rows.append([model, str(len(pivot)),
                         num(quadratic_weighted_kappa(pivot["with_gs"], pivot["without_gs"]), 2),
                         num(correlation(pivot["with_gs"], pivot["without_gs"])["r"], 2),
                         num(100 * exact_agreement(pivot["with_gs"], pivot["without_gs"]), 0) + r"\%"])
    if rows:
        save("judge_gs_vs_nogs.tex", latex_table(
            rows, ["Modello", "Casi", "Kappa pesata", "Spearman", "Accordo esatto"],
            "Accordo tra il giudizio con Gold Standard e quello senza Gold Standard dello stesso modello.",
            "tab:judge-gs-vs-nogs"))


def pooled_sensitivity(df: pd.DataFrame, score_col: str) -> float:
    """-Spearman(severity effettiva, punteggio) su tutti i casi di df, tipi di errore mescolati."""
    r = correlation(df["effective_severity"], df[score_col], "spearman")["r"]
    return -r if not math.isnan(r) else float("nan")


def table_same_cases(cases: pd.DataFrame, judges: pd.DataFrame, metric_cols: list[str]) -> pd.DataFrame | None:
    """Metriche e giudici a confronto sugli STESSI casi.

    La tabella delle sensibilità delle metriche è calcolata per tipo di errore su tre livelli
    di gravità, quella dei giudici su un sottoinsieme (GS intatto + perturbazioni a
    JUDGE_SEVERITY, tipi mescolati): i due numeri non sono confrontabili. Qui le metriche
    vengono ricalcolate sul sottoinsieme dei giudici, con lo stesso metodo.
    """
    if judges.empty or not metric_cols:
        return None
    subset = cases[(cases["kind"] == "perturbation")
                   & ((cases["ptype"] == "none") | (cases["severity"] == config.JUDGE_SEVERITY))]
    records = []
    for m in metric_cols:
        records.append({"name": METRICS[m], "kind": "metrica", "n": len(subset),
                        "sensitivity": pooled_sensitivity(subset, m),
                        "ci": bootstrap_by_document(subset, lambda d, m=m: pooled_sensitivity(d, m))})
    for (model, mode), sub in judges[judges["valid_json"]].groupby(["model", "mode"], sort=False):
        pert = sub[sub["kind"] == "perturbation"]
        records.append({"name": f"{model} ({MODES.get(mode, mode)})", "kind": "giudice", "n": len(pert),
                        "sensitivity": pooled_sensitivity(pert, "score"),
                        "ci": bootstrap_by_document(pert, lambda d: pooled_sensitivity(d, "score"))})
    frame = pd.DataFrame(records).sort_values("sensitivity", ascending=False)
    rows = [[r.name, r.kind, str(r.n), num(r.sensitivity, 2), f"[{num(r.ci[0], 2)}; {num(r.ci[1], 2)}]"]
            for r in frame.itertuples()]
    save("same_cases.tex", latex_table(
        rows, ["Valutatore", "Tipo", "Casi", "Sensibilità", "IC 95\\%"],
        "Metriche e giudici LLM a confronto sugli stessi casi (Gold Standard intatto e "
        "perturbazioni a gravità 0,5): sensibilità alla gravità dell'errore con intervallo "
        "di confidenza al 95\\% (bootstrap sui documenti).", "tab:same-cases", align="llccc"))
    return frame


# ---------------------------------------------------------------------------
# D. Grafici
# ---------------------------------------------------------------------------

def _style(ax) -> None:
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(TEXT_SECONDARY)
    ax.tick_params(colors=TEXT_SECONDARY, labelsize=8)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def fig_num(x, digits: int = 2) -> str:
    """Come num(), ma con il segno meno tipografico: per le etichette dei grafici."""
    return num(x, digits).replace("-", "\u2212")


def figure_sensitivity_curves(cases: pd.DataFrame, metric_cols: list[str]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter

    pert = cases[cases["kind"] == "perturbation"]
    if pert.empty or not metric_cols:
        return
    # Dimensioni pari alla larghezza del testo della tesi (circa 13 cm): i caratteri
    # vengono stampati alla loro dimensione reale. Cinque pannelli su due righe,
    # la sesta casella ospita la legenda.
    fig, axes = plt.subplots(2, 3, figsize=(5.4, 4.0), sharex=True, sharey=True)
    axes = axes.ravel()
    xs = [0.0] + config.SEVERITIES
    comma = FuncFormatter(lambda v, _: fig_num(v, 1))
    for ax, (ptype, title) in zip(axes, PTYPES.items()):
        sub = pert[pert["ptype"].isin(["none", ptype])]
        for k, m in enumerate(metric_cols):
            ys = [sub[sub["severity"] == x][m].mean() for x in xs]
            ax.plot(xs, ys, color=SERIES_COLORS[k], marker=MARKERS[k], markersize=3.5,
                    linewidth=1.6, label=METRICS[m])
        ax.set_title(title, fontsize=9, color=TEXT_PRIMARY)
        ax.set_xticks(xs)
        ax.set_xticklabels([fig_num(x, 2) for x in xs])
        ax.set_ylim(0, 1.02)
        ax.yaxis.set_major_formatter(comma)
        _style(ax)
        ax.tick_params(labelsize=7.5)
    for ax in axes[3:5]:
        ax.set_xlabel("gravità", fontsize=8, color=TEXT_SECONDARY)
    for ax in (axes[0], axes[3]):
        ax.set_ylabel("punteggio medio", fontsize=8, color=TEXT_SECONDARY)
    handles, labels = axes[0].get_legend_handles_labels()
    axes[5].axis("off")
    axes[5].legend(handles, labels, loc="center", frameon=False, fontsize=8.5)
    # il pannello vuoto non deve nascondere le etichette dell'asse x del terzo grafico
    axes[2].tick_params(labelbottom=True)
    axes[2].set_xlabel("gravità", fontsize=8, color=TEXT_SECONDARY)
    fig.tight_layout()
    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    out = config.FIGURES_DIR / "sensitivity_curves.pdf"
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=200)
    plt.close(fig)
    print(f"  grafico: {out}")


def figure_correlation_matrix(cases: pd.DataFrame, judges: pd.DataFrame, metric_cols: list[str]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib.ticker import FuncFormatter

    if judges.empty or not metric_cols:
        return
    wide = cases.set_index("case_id")[metric_cols].rename(columns=METRICS)
    for (model, mode), sub in judges[judges["valid_json"]].groupby(["model", "mode"], sort=False):
        wide[f"{model} ({MODES.get(mode, mode)})"] = sub.set_index("case_id")["score"]
    judged = judges["case_id"].unique()
    corr = wide.loc[wide.index.intersection(judged)].corr(method="spearman")

    # divergente: due tinte + grigio neutro al centro
    cmap = LinearSegmentedColormap.from_list("div", ["#eb6834", "#f2f1ee", "#2a78d6"])
    n = len(corr)
    # Larghezza pari a quella del testo della tesi: i caratteri restano leggibili.
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    im = ax.imshow(corr.values, cmap=cmap, vmin=-1, vmax=1)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(corr.columns, rotation=55, ha="right", rotation_mode="anchor",
                       fontsize=7, color=TEXT_PRIMARY)
    ax.set_yticklabels(corr.index, fontsize=7, color=TEXT_PRIMARY)
    ax.tick_params(length=0)
    for i in range(n):
        for j in range(n):
            v = corr.values[i, j]
            if not math.isnan(v):
                color = "white" if abs(v) > 0.7 else TEXT_PRIMARY
                ax.text(j, i, fig_num(v, 2), ha="center", va="center", fontsize=5.8, color=color)
    # separa visivamente metriche e giudici
    k = len(metric_cols)
    ax.axhline(k - 0.5, color=TEXT_PRIMARY, linewidth=0.8)
    ax.axvline(k - 0.5, color=TEXT_PRIMARY, linewidth=0.8)
    for side in ax.spines.values():
        side.set_visible(False)
    cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cbar.ax.tick_params(labelsize=7)
    cbar.ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: fig_num(v, 2)))
    cbar.outline.set_visible(False)
    fig.tight_layout()
    out = config.FIGURES_DIR / "correlation_matrix.pdf"
    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=200)
    plt.close(fig)
    print(f"  grafico: {out}")


# ---------------------------------------------------------------------------
# E. Riepilogo in JSON (letto dall'API /experiment_results e dalla Web UI)
# ---------------------------------------------------------------------------

def _clean(value):
    if isinstance(value, float) and math.isnan(value):
        return None
    return round(value, 4) if isinstance(value, float) else value


def write_summary(cases: pd.DataFrame, judges: pd.DataFrame, metric_cols: list[str],
                  sens: pd.DataFrame | None, judge_stats: pd.DataFrame | None) -> None:
    import json

    parser = cases[cases["kind"] == "parser"]
    summary = {
        "metrics": {m: METRICS[m] for m in metric_cols},
        "perturbations": PTYPES,
        "parser_quality": {
            DOMAINS.get(d, d): {METRICS[m]: _clean(float(sub[m].mean())) for m in metric_cols}
            for d, sub in parser.groupby("domain")
        },
        "sensitivity": {} if sens is None else {
            METRICS[m]: {PTYPES.get(p, p): _clean(float(sens.loc[m, p])) for p in list(PTYPES) + ["media"]}
            for m in metric_cols
        },
        "judges": [] if judge_stats is None else [
            {k: _clean(v) for k, v in rec.items()} for rec in judge_stats.to_dict("records")
        ],
        "n_cases": int(len(cases)),
        "n_judgements": int(len(judges)),
    }
    path = config.RESULTS_DIR / "summary.json"
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  riepilogo: {path}")


# ---------------------------------------------------------------------------

def main() -> None:
    cases, judges, metric_cols = load_frames()
    print(f"Casi: {len(cases)} | metriche: {metric_cols} | giudizi: {len(judges)}")
    table_parser_quality(cases, metric_cols)
    sens = table_sensitivity(cases, metric_cols)
    if sens is not None:
        print("\nSensibilità delle metriche (1 = ottima, 0 = cieca):")
        print(sens.round(2).to_string())
    judge_stats = table_judges(judges)
    if judge_stats is not None:
        print("\nGiudici:")
        print(judge_stats.round(2).to_string(index=False))
    table_judge_agreement(judges)
    same = table_same_cases(cases, judges, metric_cols)
    if same is not None:
        print("\nMetriche e giudici sugli stessi casi (sensibilità e IC 95%):")
        for r in same.itertuples():
            print(f"  {r.name:<28} {r.sensitivity:6.2f}  [{r.ci[0]:.2f}, {r.ci[1]:.2f}]  n={r.n}")
    figure_sensitivity_curves(cases, metric_cols)
    figure_correlation_matrix(cases, judges, metric_cols)
    write_summary(cases, judges, metric_cols, sens, judge_stats)


if __name__ == "__main__":
    main()
