# 1
# Завернуть код из первой задачи прошлого домашнего задания в вечный цикл.

while True:
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст: "))
    greeting = f"Приветсвую, {name}!"

    if age < 18:
        print(f"{greeting} У вас нет доступа к взрослому контетнту.")
    elif age == 18:
        print(f"{greeting} Поздравляю с совершеннолетием! У вас нет доступа к взрослому контенту.")
    else:
        print(f"{greeting} У вас есть доступ к взрослому контенту.")
