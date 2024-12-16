from collections import UserString

# Напишите определение класса StringWithSort


# Проверки для класса StringWithSort

# Пример использования:
class StringWithSort:
    def __init__(self, s: str):
        self.data = UserString(s)

    def sort(self, key=None, reverse=False):
        temp = sorted(str(self.data), key=key, reverse=reverse)
        # Соединяем отсортированные символы в строку
        return ''.join(temp)






s = StringWithSort("Golden retriver")

assert s.sort() == ' Gdeeeilnorrrtv'
assert s.data == 'Golden retriver'

assert s.sort(reverse=True) == 'vtrrronlieeedG '
#
new_s = StringWithSort('HelloMyFriend')
# # При обычной сортироки сперва идут заглавные буквы потом строчные
assert new_s.sort() == 'FHMdeeillnory'
# # Сортировка с ключом lower, который во время сравнения все буквы делает строчными
assert new_s.sort(key=str.lower) == 'deeFHillMnory'