# 1
# Написать лямбда-функцию определяющую чётное/нечётное. Функция принимает
# параметр(число) и если чётное, то выдаёт слово "чётное", если нет - то "нечётное"

num = int(input("Введите число:"))
is_even = lambda x: "чётное" if x % 2 == 0 else "нечётное"
print(is_even(num))
