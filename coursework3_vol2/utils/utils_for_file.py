import json


def load_data():
    """
    получает файл джейсон
    :return: возвращает список со словарями
    """
    with open("../data/operations.json", "r", encoding="utf-8") as f:
        return json.load(f)

print(type(load_data()))