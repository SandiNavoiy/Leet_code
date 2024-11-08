from collections import defaultdict


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    def is_money_enough(self, amount):
        return self.balance >= amount

    def payment(self, amount):
        if self.is_money_enough(amount):
            self.balance -= amount
        else:
            print("Не хватает средств на балансе. Пополните счет")


class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = defaultdict()
        self.__total = 0

    def add(self, product, value=1):
        self.__total = self.__total + value * product.price
        if product.name not in self.goods:
            self.goods[product.name] = [value]
        else:
            self.goods[product.name].append(value)

    def print_check(self):
        print("---Your check---")
        for product_name, values in self.goods.items():
            print(
                f"{product_name} {product.price} {values[0]} {values[0] * product.price}"
            )
        print(f"---Total: {self.__total}---")


billy = User("billy@rambler.ru")

lemon = Product("lemon", 20)
carrot = Product("carrot", 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
print(cart_billy.goods)
# cart_billy.print_check()
# """ Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 2 40
# ---Total: 70---"""
# cart_billy.add(lemon, 3)
# cart_billy.print_check()
# """ Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---"""
# cart_billy.remove(lemon, 6)
# cart_billy.print_check()
# """ Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# ---Total: 30---"""
# print(cart_billy.total)  # 30
# cart_billy.add(lemon, 5)
# cart_billy.print_check()
# """ Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---"""
# cart_billy.order()
# """ Печатает текст ниже
# Не хватает средств на балансе. Пополните счет
# Проблема с оплатой"""
# cart_billy.user.deposit(150)
# cart_billy.order()  # Заказ оплачен
# print(cart_billy.user.balance)  # 20
