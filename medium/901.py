class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack.pop()[1]

        self.stack.append((price, counter))
        return counter


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
price = 5
param_1 = obj.next(price)
