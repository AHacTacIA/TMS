# Создать 2 класса truck и car, которые являются наследниками класса auto. Класс
# truck имеет дополнительный обязательный атрибут max_load. Переопределённый
# метод move, перед появлением надписи "move" выводит надпись "attention", его
# реализацию сделать при помощи оператора super. А так же дополнительный метод
# load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и
# снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
# max_speed и при вызове метода move, после появления надписи "move" должна
# появится надпись "max speed is <max_speed>". Создать по 2 объекта для каждого
# из классов truck и car, проверить все их методы и атрибуты
import time
from task1 import Auto


class Truck(Auto):

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load


class Car(Auto):
    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed


car1 = Car("Lamborghini", 5, "Urus", 305, "black", 2200)
car2 = Car("Volkswagen", 1, "Taos", 180, "Gray")

truck1 = Truck("Iveco", 10, "STRALIS NP", 13000, "blue")
truck2 = Truck("Man", 15, "TGL", 26000)

print(f"Brand is {car1.brand}, age is {car1.age}, mark is {car1.mark}, max speed is {car1.max_speed}, color is {car1.color}, weight is {car1.weight}")
car2.birthday()
print(f"Brand is {car2.brand}, new age is {car2.age}, mark is {car2.mark}, max speed is {car2.max_speed}, color is {car2.color}, weight is {car2.weight}")

car1.move()
car1.stop()

truck1.birthday()
print(f"Brand is {truck1.brand}, new age is {truck1.age}, mark is {truck1.mark}, max load is {truck1.max_load}, color is {truck1.color}, weight is {truck1.weight}")
print(f"Brand is {truck2.brand}, age is {truck2.age}, mark is {truck2.mark}, max load is {truck2.max_load}, color is {truck2.color}, weight is {truck2.weight}")
truck1.load()
truck2.move()
