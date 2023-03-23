# 3*
# Сделать программу, в которой нужно будет угадывать число

import random

while True:
    num = random.randint(1, 100)
    num_attempts = 1
    while True:
        choice = int(input("Введите число от 1 до 100: "))
        if num == choice:
            print(f"Вы угадали число за {num_attempts} попыток")
            break
        elif num < choice:
            print("Вы не угадали число. Загаданное число меньше")
            num_attempts += 1
        else:
            print("Вы не угадали число. Загаданное число больше")
            num_attempts += 1
    print("Новая игра")
    