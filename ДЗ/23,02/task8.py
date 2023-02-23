# Пусть в программе хранится список друзей:
# friends = ['Egor', 'Liza', 'Vanya', 'Yana']
# При запуске программа просит ввести имя, и проверяет, есть ли оно в списке.
# Если есть, вывести сообщение 'У меня есть друг <имя>',
# если нет, вывести 'У меня нет друга с именем <имя>'.

friends = ['Egor', 'Liza', 'Vanya', 'Yana']
name = input("Enter name: ")
if name in friends:
    print(f"I have friend {name}")
else:
    print(f"I don't have a friend with a name {name}")
