# 2
# Добавить обработку исключений в следующие задания:
# 2 (из ДЗ номер 5)
# Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.


def check_even(num: int = None) -> bool | None:
    try:
        if num % 2 == 0:
            return True
        else:
            return False
    except (ValueError, TypeError):
        print("Введённые данные не являются числом")


def print_n(n: int = None) -> None:
    try:
        for num in range(0, n):
            if num % 7 == 0 and num % 4 == 0 and num != 0:
                return
            elif check_even(num):
                print(num * num, end=" ")
            else:
                print(num, end=" ")
    except (ValueError, TypeError):
        print("\nВведённые данные не являются числом")


print(check_even(9))
print(check_even("9"))
print(check_even())

print_n()
print_n(8)
print_n("8")
