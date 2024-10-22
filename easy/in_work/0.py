class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, (BankAccount, Numbers)):
            return self.balance + other.balance if isinstance(other, BankAccount) else self.balance + other._values
        elif isinstance(other, (int, float)):
            return self.balance + other

    def __radd__(self, other):
        if isinstance(other, (BankAccount, Numbers)):
            return other.balance + self.balance if isinstance(other, BankAccount) else other._values + self.balance
        elif isinstance(other, (int, float)):
            return other + self.balance


class Numbers:
    def __init__(self, values: list):
        self._values = sum(values)

    def __add__(self, other):
        if isinstance(other, (Numbers, BankAccount)):
            return self._values + other.balance if isinstance(other, BankAccount) else self._values + other._values
        elif isinstance(other, (int, float)):
            return self._values + other

    def __radd__(self, other):
        if isinstance(other, (Numbers, BankAccount)):
            return self._values + other.balance if isinstance(other, BankAccount) else self._values + other._values
        elif isinstance(other, (int, float)):
            return self._values + other


lst = [
    BankAccount('Jack', 1000),
    Numbers([1, 2, 3, 4, 5]),
    BankAccount('Ivan', 30),
    7.5,
    Numbers([10, 20, 30, 40, 50]),
    BankAccount('Frank', 2000),
    10
]
print(sum(lst))


#
# lst = [4, BankAccount('Petr', 100), 5]
# assert sum(lst) == 109
#
# lst = [500, BankAccount('Vanya', 200), 7, BankAccount('Ivan', 300), 3]
# assert sum(lst) == 1010
#
# lst = [
#     BankAccount('Vanya', 20),
#     BankAccount('Ivan', 30),
#     BankAccount('Frank', 40),
# ]
# assert sum(lst) == 90
#
# lst = [
#     Numbers([10, 20, 10]),
#     BankAccount('Ivan', 30),
#     Numbers([30, 40]),
# ]
# assert sum(lst) == 140
#
# lst = [
#     BankAccount('Jack', 1000),
#     Numbers([1, 2, 3, 4, 5]),
#     BankAccount('Ivan', 30),
#     7.5,
#     Numbers([10, 20, 30, 40, 50]),
#     BankAccount('Frank', 2000),
#     10
# ]
# assert sum(lst) == 3212.5
#
# lst = [
#     Numbers([1, 2, 3, 4, 5]),
#     Numbers([10, 20, 30, 40, 50]),
#     Numbers([35]),
# ]
# assert sum(lst) == 200
#
# lst = [
#     10,
#     Numbers([1, 2, 3, 4, 5]),
#     12.5,
#     Numbers([10, 20, 30, 40, 50]),
#     39,
#     Numbers([35]),
# ]
# assert sum(lst) == 261.5