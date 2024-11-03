from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    cost: int = field(repr=False)


@dataclass
class Promo:
    kod: str
    promo: int = field(repr=False)
    spisok: List[Product] = field(default_factory=list, repr=False)

    def is_applicable(self, product: Product):
        # Промокод применим ко всей корзине, если список товаров пустой
        return not self.spisok or product in self.spisok


class Cart:
    def __init__(self):
        self.products = []
        self.n = 0
        self.flag = False
        self.promo = None

    def add_product(self, product, quantity=1):
        # Добавляем продукт и его количество в корзину
        for _ in range(quantity):
            self.products.append(product)
        print(f"Добавлено: {quantity} x {product.name}")

    def apply_discount(self, n):
        if n > 100 or n < 0:
            raise ValueError("Неправильное значение скидки")
        self.n = n

    def get_total(self):
        total = 0
        for product in self.products:
            total += product.cost

        if self.n:
            # Применяем общую скидку на корзину, если она задана
            return total * (100 - self.n) / 100

        if self.promo and self.flag:
            # Применение промокода, если промокод активен
            discount_total = 0
            for product in self.products:
                if self.promo.is_applicable(product):
                    discount_total += product.cost * (100 - self.promo.promo) / 100
                else:
                    discount_total += product.cost
            return discount_total

        return total

    def apply_promo(self, promo_code):
        global ACTIVE_PROMO
        for promo in ACTIVE_PROMO:
            if promo.kod == promo_code:
                self.promo = promo
                self.flag = True
                print(f"Промокод {promo_code} успешно применен")
                return
        self.flag = False
        print(f"Промокод {promo_code} не найден")


# Примеры использования
book = Product("Книга", 100.0)
usb = Product("Флешка", 50.0)
pen = Product("Ручка", 10.0)

# Определение активных промокодов
ACTIVE_PROMO = [
    Promo("new", 20, [pen]),  # Промокод 20% на ручку
    Promo("all_goods", 30),  # Промокод 30% на все товары
]

cart = Cart()
cart.add_product(book, 2)  # Добавить 2 книги
cart.add_product(pen)  # Добавить 1 ручку
print("Общая сумма без скидок:", cart.get_total())

# Применение промокода на 20% для ручки
cart.apply_promo("new")
print("Сумма с промокодом 'new':", cart.get_total())
