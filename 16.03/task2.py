# Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в
# качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл

import json


def get_data() -> dict:
    print("Введите в строчку через пробел значения: id, имя, возраст. Если хотите остановить запись введите 0")
    strings = [input("Введите 1 строку: ")]
    while strings[-1] != "0":
        strings.append(input(f"Введите новую строку: "))
    strings = strings[:-1]
    ids = []
    name_age = []
    for string in strings:
        words = string.split()
        ids.append(int(words[0]))
        name_age.append((words[1], int(words[2])))
    info = {}

    for i in range(len(ids)):
        info[ids[i]] = name_age[i]
    return info


json_info = get_data()
with open("text1.json", "w") as json_file:
    json.dump(json_info, json_file, indent=4)
