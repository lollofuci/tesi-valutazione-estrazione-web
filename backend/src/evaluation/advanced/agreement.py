"""Misure di correlazione e di accordo tra metriche e giudici."""

from __future__ import annotations

import numpy as np
from scipy import stats


def _clean(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    keep = ~(np.isnan(x) | np.isnan(y))
    return x[keep], y[keep]


def correlation(x, y, method: str = "spearman") -> dict[str, float]:
    """Correlazione con p-value; method in {'spearman', 'kendall', 'pearson'}."""
    x, y = _clean(x, y)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return {"r": float("nan"), "p": float("nan"), "n": int(len(x))}
    func = {"spearman": stats.spearmanr, "kendall": stats.kendalltau, "pearson": stats.pearsonr}[method]
    r, p = func(x, y)
    return {"r": float(r), "p": float(p), "n": int(len(x))}


def bootstrap_ci(x, y, method: str = "spearman", n_boot: int = 1000,
                 alpha: float = 0.05, seed: int = 42) -> tuple[float, float]:
    """Intervallo di confidenza bootstrap (percentile) della correlazione."""
    x, y = _clean(x, y)
    if len(x) < 3:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(x), len(x))
        r = correlation(x[idx], y[idx], method)["r"]
        if not np.isnan(r):
            values.append(r)
    if not values:
        return float("nan"), float("nan")
    return float(np.percentile(values, 100 * alpha / 2)), float(np.percentile(values, 100 * (1 - alpha / 2)))


def quadratic_weighted_kappa(a, b, min_rating: int = 1, max_rating: int = 5) -> float:
    """Kappa di Cohen con pesi quadratici: accordo tra due giudici su scala 1-5,
    corretto per l'accordo dovuto al caso (1 = accordo perfetto, 0 = casuale)."""
    a, b = _clean(a, b)
    if len(a) == 0:
        return float("nan")
    a = a.astype(int) - min_rating
    b = b.astype(int) - min_rating
    k = max_rating - min_rating + 1
    observed = np.zeros((k, k))
    for i, j in zip(a, b):
        observed[i, j] += 1
    expected = np.outer(observed.sum(axis=1), observed.sum(axis=0)) / len(a)
    weights = np.array([[(i - j) ** 2 for j in range(k)] for i in range(k)]) / (k - 1) ** 2
    denom = (weights * expected).sum()
    if denom == 0:
        return float("nan")
    return float(1 - (weights * observed).sum() / denom)


def exact_agreement(a, b) -> float:
    """Frazione di casi in cui due giudici danno esattamente lo stesso punteggio."""
    a, b = _clean(a, b)
    return float(np.mean(a == b)) if len(a) else float("nan")


def correlation_matrix(df, columns: list[str], method: str = "spearman"):
    """Matrice di correlazione (DataFrame) tra le colonne indicate."""
    return df[columns].corr(method=method)
