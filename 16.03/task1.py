# Вести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
# файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
# редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
# строки, каждая из которых должна начинаться с новой строки.


strings = [input(f"Введите {i + 1} строку: ") for i in range(4)]

with open("text.txt", "w") as file:
    file.write(strings[0] + "\n")
    file.write(strings[1] + "\n")

with open("text.txt", "a") as file:
    file.write(strings[2] + "\n")
    file.write(strings[3])
    