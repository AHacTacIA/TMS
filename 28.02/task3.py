# 3*
# Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
# либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
# Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
# Бот выбрал ножницы, вы проиграли!
# Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами

import random
while True:
    bot_choice = random.randint(0, 2)
    player_choice = int(input("Введите 0, если выбрали камень\n"
                              "Введите 1, если выбрали ножницы\n"
                              "Введите 2, если выбрали бумагу\n"))

    if player_choice == 0:
        print("Вы выбрали камень.")
    elif player_choice == 1:
        print("Вы выбрали ножницы")
    else:
        print("Вы выбрали бумагу")

    if bot_choice == 0:
        str_bot = "Бот выбрал камень."
    elif bot_choice == 1:
        str_bot = "Бот выбрал ножницы."
    else:
        str_bot = "Бот выбрал бумагу."

    print("Камень, ножницы, бумага. 1! 2! 3!")
    if bot_choice == player_choice:
        print(f"{str_bot} Ничья")
    elif (bot_choice == 0 and player_choice == 2) or (bot_choice == 1 and player_choice == 0) or (
            bot_choice == 2 and player_choice == 1):
        print(f"{str_bot} Вы выйграли!")
    else:
        print(f"{str_bot} Вы проиграли!")
