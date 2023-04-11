# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.
import random

class EndlessIterator:
    def __init__(self, start_num: int = 0, end_num: int = None, stop_num: int = None):
        self._start_num = start_num
        self._end_num = end_num
        self._stop_num = stop_num

    def __iter__(self):
        return self

    def __next__(self):
        if self._end_num is None or self._start_num > self._end_num:
            raise StopIteration
        result = random.randint(self._start_num, self._end_num)
        if result == self._stop_num:
            print(result)
            raise StopIteration
        return result


def endless_generator(start_num: int, end_num: int, stop_num: int):
    while True:
        if start_num > end_num:
            break
        result = random.randint(start_num, end_num)
        if result == stop_num:
            print(result)
            break
        yield result


rand_nums = EndlessIterator(15, 50, 30)
for num in rand_nums:
    print(num, end=' ')

rand_nums = endless_generator(15, 50, 30)
for num in rand_nums:
    print(num, end=' ')
