from utils.utils_for_file import load_data
from utils.utils_for_data import slice_data, magic_with_date, magic_with_N_card, magic_with_N_account


def output_banking_operation(data: list):
    for i in data:
        print(f'{magic_with_date(i["date"])} {i["description"]}\n'
              f'{magic_with_N_card(i["from"]) if i.get("from")!=None else ""} -> '
              f'{magic_with_N_account(i["to"])}\n{i["operationAmount"]["amount"]} '
              f'{i["operationAmount"]["currency"]["name"]}\n')

output_banking_operation(slice_data(load_data("data/operations.json")))
