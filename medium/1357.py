class Cashier:
    def __init__(self, n, discount, products, prices):
        self.count, self.n, self.discount = 0, n, discount
        self.dict1 = {i: j for i, j in zip(products, prices)}

    def getBill(self, product, amount):
        self.count += 1

        total = 0

        for i, j in zip(product, amount):
            total += self.dict1[i] * j

        return (
            total if self.count % self.n != 0 else total * ((100 - self.discount) / 100)
        )


# Your Cashier object will be instantiated and called as such:
n = 3
discount = 50
products = [1, 2, 3, 4, 5, 6, 7]
prices = [100, 200, 300, 400, 300, 200, 100]
obj = Cashier(n, discount, products, prices)
product = [1, 2]
amount = [1, 2]

param_1 = obj.getBill(product, amount)
