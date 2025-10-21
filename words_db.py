import os
import json

DB_PATH = "words_db.json"

def load_words_db():

    """Carrega o banco de dados de palavras a partir do arquivo JSON."""
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r", encoding="utf-8") as f:
            try:
                words = json.load(f)

                return words
            except json.JSONDecodeError:
                words = {}
    else:
        words = {}
        return words

def save_words_db(db):

    """Salva o banco de dados de palavras no arquivo JSON."""

    with open(DB_PATH, "w", encoding="utf-8") as arq:
        json.dump(db, arq, ensure_ascii=False, indent=4)


def create_words_item(item_dict:dict):

    """"Adiciona um novo dicionario ao banco de dados(json)"""

    db = load_words_db()
    db.append(item_dict)  
    save_words_db(db)


    