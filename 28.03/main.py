# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.
import time
import datetime as dt


class AccountHistory:
    def __init__(self, balance: float, name: str = "пополнение"):
        self.name = name
        self.summa = balance
        self.date = dt.datetime.isoformat(dt.datetime.now())

    def __repr__(self):
        return 'History(%s, %s, %s)' % (self.name, self.summa, self.date)


class BankAccount:
    def __init__(self, balance: float = 0):
        self._balance = balance
        self.history = [AccountHistory(balance)]

    def __str__(self):
        return f"{self._balance},{self.history}"

    def balance_top_up(self, balance: float) -> None:
        self._balance += balance
        self.history.append(AccountHistory(balance))

    def remove_from_balance(self, balance: float) -> None:
        self._balance -= balance
        self.history.append(AccountHistory(balance, "снятие"))


account1 = BankAccount()
account1.balance_top_up(10)
print(account1)
account1.balance_top_up(150)
time.sleep(1)
account1.remove_from_balance(50)
print(account1)

