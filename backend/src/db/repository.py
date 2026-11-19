"""Query riusabili sul database, usate dagli endpoint del backend."""

from db.connection import get_connection


def _rows_as_dicts(cursor) -> list[dict]:
    columns = [desc[0] for desc in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_web_resource(url: str) -> dict | None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT url, domain, title, html_text FROM web_resources WHERE url = ?", (url,))
        rows = _rows_as_dicts(cur)
        cur.close()
        return rows[0] if rows else None
    finally:
        conn.close()


def get_gold_standard_entry(url: str) -> dict | None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT w.url, w.domain, w.title, w.html_text, g.gold_text "
            "FROM gold_standard g JOIN web_resources w ON g.url = w.url WHERE g.url = ?",
            (url,),
        )
        rows = _rows_as_dicts(cur)
        cur.close()
        return rows[0] if rows else None
    finally:
        conn.close()


def get_full_gold_standard(domain: str) -> list[dict]:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT w.url, w.domain, w.title, w.html_text, g.gold_text "
            "FROM gold_standard g JOIN web_resources w ON g.url = w.url "
            "WHERE w.domain = ? ORDER BY w.url",
            (domain,),
        )
        rows = _rows_as_dicts(cur)
        cur.close()
        return rows
    finally:
        conn.close()


def get_gold_standard_urls(domain: str) -> list[str]:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT w.url FROM gold_standard g JOIN web_resources w ON g.url = w.url "
            "WHERE w.domain = ? ORDER BY w.url",
            (domain,),
        )
        urls = [row[0] for row in cur.fetchall()]
        cur.close()
        return urls
    finally:
        conn.close()


def add_web_resource(url: str, domain: str, title: str, html_text: str) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO web_resources (url, domain, title, html_text) VALUES (?, ?, ?, ?) "
            "ON DUPLICATE KEY UPDATE domain=VALUES(domain), title=VALUES(title), html_text=VALUES(html_text)",
            (url, domain, title, html_text),
        )
        cur.close()
    finally:
        conn.close()


def add_gold_standard(url: str, gold_text: str) -> None:
    # La FK richiede che la web_resource esista gia'.
    if get_web_resource(url) is None:
        raise LookupError("URL non presente in web_resources")
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO gold_standard (url, gold_text) VALUES (?, ?) "
            "ON DUPLICATE KEY UPDATE gold_text=VALUES(gold_text)",
            (url, gold_text),
        )
        cur.close()
    finally:
        conn.close()


def delete_web_resource(url: str) -> bool:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM web_resources WHERE url = ?", (url,))
        affected = cur.rowcount
        cur.close()
        return affected > 0
    finally:
        conn.close()


def delete_gold_standard(url: str) -> bool:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM gold_standard WHERE url = ?", (url,))
        affected = cur.rowcount
        cur.close()
        return affected > 0
    finally:
        conn.close()


def save_parsed_document(url: str, title: str, parsed_text: str) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO parsed_documents (url, title, parsed_text) VALUES (?, ?, ?) "
            "ON DUPLICATE KEY UPDATE title=VALUES(title), parsed_text=VALUES(parsed_text)",
            (url, title, parsed_text),
        )
        cur.close()
    finally:
        conn.close()


def save_evaluation(url: str, precision: float, recall: float, f1: float) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO evaluations (url, precision_score, recall_score, f1_score) VALUES (?, ?, ?, ?) "
            "ON DUPLICATE KEY UPDATE precision_score=VALUES(precision_score), "
            "recall_score=VALUES(recall_score), f1_score=VALUES(f1_score)",
            (url, precision, recall, f1),
        )
        cur.close()
    finally:
        conn.close()


def save_judge_evaluation(url: str, model_name: str, judge_score: int, judge_feedback: str) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO judge_evaluations (url, model_name, judge_score, judge_feedback) VALUES (?, ?, ?, ?) "
            "ON DUPLICATE KEY UPDATE model_name=VALUES(model_name), "
            "judge_score=VALUES(judge_score), judge_feedback=VALUES(judge_feedback)",
            (url, model_name, judge_score, judge_feedback),
        )
        cur.close()
    finally:
        conn.close()


def save_advanced_evaluation(url: str, metrics: dict) -> None:
    """Salva le metriche avanzate di una pagina (tesi, personalizzazione 4a)."""
    def f(name: str):
        return metrics[name]["f"] if name in metrics else None

    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO advanced_evaluations (url, token_f, rougeL_f, chrf_f, meteor_f, bertscore_f) "
            "VALUES (?, ?, ?, ?, ?, ?) "
            "ON DUPLICATE KEY UPDATE token_f=VALUES(token_f), rougeL_f=VALUES(rougeL_f), "
            "chrf_f=VALUES(chrf_f), meteor_f=VALUES(meteor_f), "
            "bertscore_f=COALESCE(VALUES(bertscore_f), bertscore_f)",
            (url, f("token"), f("rougeL"), f("chrf"), f("meteor"), f("bertscore")),
        )
        cur.close()
    finally:
        conn.close()


def avg_advanced_per_domain() -> dict:
    """Media delle metriche avanzate per dominio."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT w.domain, AVG(a.rougeL_f), AVG(a.chrf_f), AVG(a.meteor_f), AVG(a.bertscore_f) "
            "FROM advanced_evaluations a JOIN web_resources w ON a.url = w.url GROUP BY w.domain"
        )
        result = {}
        for domain, rouge, chrf, meteor, bert in cur.fetchall():
            result[domain] = {
                "rougeL_f": round(rouge, 4) if rouge is not None else None,
                "chrf_f": round(chrf, 4) if chrf is not None else None,
                "meteor_f": round(meteor, 4) if meteor is not None else None,
                "bertscore_f": round(bert, 4) if bert is not None else None,
            }
        cur.close()
        return result
    finally:
        conn.close()


def count_per_domain() -> tuple[dict, dict]:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT domain, COUNT(*) FROM web_resources GROUP BY domain")
        web_counts = {row[0]: row[1] for row in cur.fetchall()}
        cur.execute(
            "SELECT w.domain, COUNT(*) FROM gold_standard g "
            "JOIN web_resources w ON g.url = w.url GROUP BY w.domain"
        )
        gs_counts = {row[0]: row[1] for row in cur.fetchall()}
        cur.close()
        return web_counts, gs_counts
    finally:
        conn.close()


def avg_eval_per_domain() -> dict:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT w.domain, AVG(e.precision_score), AVG(e.recall_score), AVG(e.f1_score) "
            "FROM evaluations e JOIN web_resources w ON e.url = w.url GROUP BY w.domain"
        )
        result = {}
        for domain, prec, rec, f1 in cur.fetchall():
            result[domain] = {
                "token_level_eval": {
                    "precision": round(prec, 4) if prec is not None else 0.0,
                    "recall": round(rec, 4) if rec is not None else 0.0,
                    "f1": round(f1, 4) if f1 is not None else 0.0,
                }
            }
        cur.close()
        return result
    finally:
        conn.close()


def avg_judge_per_domain() -> dict:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT w.domain, AVG(j.judge_score) FROM judge_evaluations j "
            "JOIN web_resources w ON j.url = w.url GROUP BY w.domain"
        )
        result = {}
        for domain, score in cur.fetchall():
            result[domain] = {"judge_score": round(score, 4) if score is not None else 0.0}
        cur.close()
        return result
    finally:
        conn.close()


def avg_judge_for_domain(domain: str) -> float:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT AVG(j.judge_score) FROM judge_evaluations j "
            "JOIN web_resources w ON j.url = w.url WHERE w.domain = ?",
            (domain,),
        )
        row = cur.fetchone()
        cur.close()
        return float(row[0]) if row and row[0] is not None else 0.0
    finally:
        conn.close()


def get_db_schema() -> dict:
    """Schema reale letto da information_schema: colonne, tipi, PK e FK."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME "
            "FROM information_schema.KEY_COLUMN_USAGE "
            "WHERE TABLE_SCHEMA = DATABASE() AND REFERENCED_TABLE_NAME IS NOT NULL"
        )
        fks = {(t, c): f"FK({ref_t}.{ref_c})" for t, c, ref_t, ref_c in cur.fetchall()}

        cur.execute(
            "SELECT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY "
            "FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = DATABASE() "
            "ORDER BY TABLE_NAME, ORDINAL_POSITION"
        )
        schema: dict = {}
        for table, column, col_type, col_key in cur.fetchall():
            descr = col_type
            if col_key == "PRI":
                descr += ", PK"
            if (table, column) in fks:
                descr += ", " + fks[(table, column)]
            schema.setdefault(table, {})[column] = descr
        cur.close()
        return schema
    finally:
        conn.close()
