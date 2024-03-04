class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """"""
        prices.sort()
        if prices[0] + prices[1] > money:
            return money
        return money - (prices[0] + prices[1])


prices = [1, 2, 2]
money = 3
s = Solution()
print(s.buyChoco(prices, money))
