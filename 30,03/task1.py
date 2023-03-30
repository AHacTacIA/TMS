# 1
# Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров
import datetime


class info_about_func:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        time = datetime.datetime.now()
        result = self.func(*args, **kwargs)
        message = f"Функция {self.func.__name__} вызвана {time}"
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


@info_about_func
def add(a: int = 0, b: int = 0) -> int:
    return a + b


print(add())
print(add(2, 3))
print(add(2, b=3))
print(add(a=2, b=3))
