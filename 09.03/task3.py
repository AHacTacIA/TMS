# 3
# При помощи функции filter() из кортежа слов отфильтровать только те, которые
# являются полиндромами.

def is_polindrom(string):
    if string == string[::-1]:
        return True
    return False


tuple_str = {'asdf', 'aba', 'efgkgfe', 'qwer'}
new_tuple = tuple(filter(is_polindrom,tuple_str))
print(new_tuple)
