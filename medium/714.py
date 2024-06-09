class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        ''''''
        sum_scoks = 0
        min_price = prices[0] + fee
        for i in prices:

            if i > min_price:
                sum_scoks = sum_scoks + i - min_price
                min_price = i
            elif i + fee < min_price:
                min_price = i + fee

        return sum_scoks

prices = [9,8,7,1,2]
fee = 3
s = Solution()
print(s.maxProfit(prices, fee))