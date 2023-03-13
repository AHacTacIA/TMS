# 2
# Дан список чисел. Вернуть список, где при помощи функции map() каждое число
# переведено в строку. В качестве функции в map использовать lambda.

list_num = [1, 85, 1, 95, -5]
new_list = list(map(lambda x: str(x), list_num))
print(new_list)
