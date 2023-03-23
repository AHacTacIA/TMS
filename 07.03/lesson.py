# Дан список чисел. Написать функцию, которая вернет сумму только положительных элементов списка

def sum_positive(list_: list[int] = None) -> int:
    if not list_ or type(list_) != list:
        return False
    else:
        sum_ = 0
        for i in range(0, len(list_)):
            if list_[i] > 0:
                sum_ += list_[i]
        return sum_


print(sum_positive([1, 2, -7, 8, 0, -9]))


# Дан список чисел. Написать функцию, которая вернет минимальное значение из списка.
# (Конкретно в этой задаче встроенную функцию min не использовать)

def find_min(list_: list[int] = []) -> int:
    if not list_ or type(list_) != list:
        return False
    min_value = list_[0]
    for num in list_:
        if min_value > num:
            min_value = num
    return min_value


print(find_min())


# Написать функцию которая печатает числа от 0 до n, n - параметр.
# Если число делится на 3, вместо числа печатает fizz, если число делится на 5, вместо числа печатает buzz.
# Если число делится и на 3 и на 5, вместо числа печатает fizzbuzz

def print_n_num(n: int = None):
    if type(n) != int:
        return False
    else:
        for i in range(0, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz", end=" ")
            elif i % 3 == 0:
                print("fizz", end=" ")
            elif i % 5 == 0:
                print("buzz", end=" ")
            else:
                print(i, end=" ")


print_n_num(20)
