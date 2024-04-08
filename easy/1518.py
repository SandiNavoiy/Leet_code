class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """"""
        return int(numBottles + (numBottles - 1) / (numExchange - 1))


numBottles = 15
numExchange = 4
s = Solution()
print(s.numWaterBottles(numBottles, numExchange))
