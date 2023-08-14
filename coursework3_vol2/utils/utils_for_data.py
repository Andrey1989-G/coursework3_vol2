from utils_for_file import load_data
def slice_data(data: list, count_id: int):
    """
    выводит последние count_id выполненных (EXECUTED) на экран.
    :param data: список со словарями
    :param count_id: количество айди для вывода
    :return: список со словарями
    """
    res = []
    for i in reversed(data):
        while len(res) != count_id:
            if i["state"] == "EXECUTED":
                res.append(i)
            else:
                break
    return list(reversed(res))

# print(slice_data(load_data(), 5))