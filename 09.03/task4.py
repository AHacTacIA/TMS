# 4
# Написать декоратор к 2-м любым функциям, который бы считал и выводил время
# их выполнения.
import time


def square(n: int) -> list:
    return [i * i for i in range(n)]


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def decorator(func):
    def inner(*args, **kwargs):
        time1 = time.time()
        result = func(*args, **kwargs)
        time2 = time.time()
        print(f'Результат = {result}\nВремя выполнения = {time2 - time1}')
        return result

    return inner


n = int(input("Введите количество элементов: "))
new_square = decorator(square)
new_square(n)

new_add = decorator(add)
new_add(5, 10)
