# Напишите определение классов Product и ShoppingCart

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


apple = Product("Apple", 1.5)
banana = Product("Banana", 0.75)
chocolate = Product("Chocolate", 2.99)


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, item):

        self._items.append(item)
        self._items = sorted(self._items, key=lambda x: (x.price, x.name))

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError("Item not found in the cart")
    def __len__(self):
        return len(self._items)

    @property
    def items(self):


        return self._items

    @property
    def total_price(self):
        return sum(item.price for item in self._items)


cart = ShoppingCart()
cart.add_item(banana)
cart.add_item(apple)
cart.add_item(chocolate)

assert len(cart) == 3

assert cart.items == [banana, apple, chocolate]
#
milk = Product('Milk', 1)
cart.add_item(milk)

assert cart.items == [banana, milk, apple, chocolate]
print("Items in the cart:", [item.name for item in cart.items])
print("Total price:", cart.total_price)
assert cart.total_price == 6.24
cart.add_item(banana)
assert len(cart) == 5
assert cart.total_price == 6.99
cart.remove_item(milk)
assert len(cart) == 4
cart.remove_item(banana)
cart.remove_item(banana)
assert len(cart) == 2
try:
    cart.remove_item(banana)
except ValueError:
    pass