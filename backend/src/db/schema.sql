-- Schema del database (MariaDB).
-- url e' VARCHAR(768): con utf8mb4 e' il massimo indicizzabile per intero,
-- necessario per poterlo usare come chiave esterna (le FK non ammettono indici prefissati).

CREATE TABLE IF NOT EXISTS web_resources (
    url        VARCHAR(768)  NOT NULL,
    domain     VARCHAR(255)  NOT NULL,
    title      VARCHAR(2048),
    html_text  LONGTEXT,
    created_at DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (url)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- gold_standard: relazione 1-a-1 con web_resources, cancellazione a cascata.
CREATE TABLE IF NOT EXISTS gold_standard (
    url        VARCHAR(768) NOT NULL,
    gold_text  LONGTEXT,
    created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (url),
    CONSTRAINT fk_gold_standard_url
        FOREIGN KEY (url) REFERENCES web_resources(url)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabelle ausiliarie: output del parser e valutazioni pre-calcolate (usate da /db_stats).
CREATE TABLE IF NOT EXISTS parsed_documents (
    url         VARCHAR(768) NOT NULL,
    title       VARCHAR(2048),
    parsed_text LONGTEXT,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (url),
    CONSTRAINT fk_parsed_documents_url
        FOREIGN KEY (url) REFERENCES web_resources(url)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS evaluations (
    url             VARCHAR(768) NOT NULL,
    precision_score DOUBLE,
    recall_score    DOUBLE,
    f1_score        DOUBLE,
    created_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (url),
    CONSTRAINT fk_evaluations_url
        FOREIGN KEY (url) REFERENCES web_resources(url)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS judge_evaluations (
    url            VARCHAR(768) NOT NULL,
    model_name     VARCHAR(255),
    judge_score    INT,
    judge_feedback TEXT,
    created_at     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (url),
    CONSTRAINT fk_judge_evaluations_url
        FOREIGN KEY (url) REFERENCES web_resources(url)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tesi (personalizzazione 4a): metriche avanzate per ogni pagina del Gold Standard.
-- bertscore_f puo' essere NULL (BERTScore e' facoltativo perche' piu' lento).
CREATE TABLE IF NOT EXISTS advanced_evaluations (
    url         VARCHAR(768) NOT NULL,
    token_f     DOUBLE,
    rougeL_f    DOUBLE,
    chrf_f      DOUBLE,
    meteor_f    DOUBLE,
    bertscore_f DOUBLE,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (url),
    CONSTRAINT fk_advanced_evaluations_url
        FOREIGN KEY (url) REFERENCES web_resources(url)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
