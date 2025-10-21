import os
import json

DB_PATH = "./words_db.json"


def load_words_db():
    """Carrega o banco de dados de palavras a partir do arquivo JSON."""
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r", encoding="utf-8") as f:
            try:
                words = json.load(f)
                return words

            except json.JSONDecodeError:
                print("Erro ao decodificar o arquivo JSON. Retornando banco de dados vazio.")
                return []
    else:
        with open(DB_PATH, "w", encoding="utf-8") as f:
            f.write("")
            words = []
            return words


def save_words_db(db):
    """Salva o banco de dados de palavras no arquivo JSON."""

    db_loaded = load_words_db()
    db_loaded.extend(db)

    with open(DB_PATH, "w", encoding="utf-8") as arq:
        json.dump(db_loaded, arq, ensure_ascii=False, indent=4)
