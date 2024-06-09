class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        ''''''
        sum_scoks = 0
        min_price = prices[0] + fee
        for i in prices:
            if i + fee < min_price:
                min_price = i +fee
            elif i + fee > min_price:
                sum_scoks = sum_scoks + i - min_price
                min_price = i

        return sum_scoks

prices = [1,3,2,8,4,9]
fee = 2
s = Solution()
print(s.maxProfit(prices, fee))