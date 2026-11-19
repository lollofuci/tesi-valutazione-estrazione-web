"""Connessione a MariaDB tramite MariaDB Connector/Python."""

import os
import time

import mariadb


def get_db_config() -> dict:
    return {
        "host": os.getenv("DB_HOST", "mariadb"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "root"),
        "database": os.getenv("DB_NAME", "lab"),
    }


def get_connection(autocommit: bool = True) -> mariadb.Connection:
    conn = mariadb.connect(**get_db_config())
    conn.autocommit = autocommit
    return conn


def wait_for_db(max_retries: int = 30, delay: float = 2.0) -> None:
    """Attende che il database sia raggiungibile all'avvio."""
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            conn = mariadb.connect(**get_db_config())
            conn.close()
            return
        except mariadb.Error as exc:
            last_error = exc
            print(f"[db] tentativo {attempt}/{max_retries}: DB non pronto, riprovo...")
            time.sleep(delay)
    raise RuntimeError(f"Database non raggiungibile dopo {max_retries} tentativi: {last_error}")


def is_alive() -> bool:
    """True se il database risponde (usata da /status)."""
    try:
        conn = mariadb.connect(**get_db_config())
        conn.close()
        return True
    except mariadb.Error:
        return False
