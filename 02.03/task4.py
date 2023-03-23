# 4*
# Ввести строку (считаем, что в начале и в конце строки нет пробелов,
# все слова в строке разделены одним пробелом). Для введенной строки
# изменить порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.
# Примеры:
# "Hello World!" -> "olleH !dlroW"
# "Let's see, how it works" -> "s'teL ,ees woh ti skrow"

string = input("Введите строку: ")
str_list = string.split()
new_str_list = list()
for i in range(len(str_list)):
    new_str_list.append(str_list[i][::-1])

new_str = " ".join(new_str_list)
print(new_str)
