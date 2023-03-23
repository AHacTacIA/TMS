# Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой
# строкой которого озоглавив каждый столбец и добавив новый столбец "телефон"
import csv
import json

with open("input.json", "r") as json_file:
    json_data = json.load(json_file)

output = ",".join([*json_data[0]]) + ",phone"
for data in json_data:
    output += f'\n{data["id"]},{data["name"]},{data["age"]}' + ','

with open("output.csv", "w") as csv_file:
    csv_file.write(output)
