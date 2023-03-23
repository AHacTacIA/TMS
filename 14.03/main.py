import datetime
from typing import Callable
from functools import wraps


# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров


def decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        time = datetime.datetime.now()
        result = func(*args, **kwargs)
        message = f"Функция {func.__name__} вызвана {time}"
        message_list = []
        if args:
            message_list.append(f"с позиционными параметрами {args}")
        if kwargs:
            message_list.append(f"с именнованными параметрами {kwargs}")
        if not message_list:
            message += " без параметров"
        else:
            message += " " + " и ".join(message_list)
        print(message)
        return result
    return inner


@decorator
def add(a: int | float = 0, b: int | float = 0) -> int | float:
    return a + b
