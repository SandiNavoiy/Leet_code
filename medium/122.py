class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """"""
        sss = 0
        temp = 0
        flag = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i] and flag == 0:
                temp = prices[i]
                flag = 1
            elif prices[i + 1] < prices[i] and flag == 1:
                sss = sss + prices[i] - temp
                temp = 0
                flag = 0

            print(sss, temp, i)
        if flag > 0:
            return sss + (prices[len(prices) - 1]) - temp

        return sss


prices = [2, 1, 2, 0, 1]
s = Solution()
print(s.maxProfit(prices))
