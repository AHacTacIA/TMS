# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.
import time
import datetime as dt
from enum import Enum


class OperationEnum(Enum):
    PLUS = "Пополнение"
    MINUS = "Снятие"


class AccountHistory:
    def __init__(self, balance: float, name: str):
        self.name = name
        self.summa = balance
        self.date = dt.datetime.isoformat(dt.datetime.now())

    def __repr__(self):
        return 'History(%s, %s, %s)' % (self.name, self.summa, self.date)


class BankAccount:
    def __init__(self, balance: float = 0):
        self._balance = balance
        self.history = [AccountHistory(balance, OperationEnum.PLUS.value)]

    def __str__(self):
        return f"{self._balance},{self.history}"

    def do_operation(self, balance: float, operation: OperationEnum):
        if operation == OperationEnum.PLUS:
            self._balance += balance
            self.history.append(AccountHistory(balance, operation.value))
        else:
            self._balance -= balance
            self.history.append(AccountHistory(balance, operation.value))

    @property
    def get_balance(self):
        return self._balance


account1 = BankAccount()
account1.do_operation(30, OperationEnum.PLUS)
print(account1)
time.sleep(1)
account1.do_operation(25, OperationEnum.MINUS)
print(account1)
time.sleep(1)
account1.do_operation(80, OperationEnum.PLUS)
print(account1)
account1.do_operation(100, OperationEnum.PLUS)
print(account1.get_balance)

