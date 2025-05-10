class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        """Максимальное количество контейнеров на судне"""

        y= 0

        for i in range(1, n*n+1):
            y = y +  w
            if y == maxWeight:

                return i
            elif y > maxWeight:

                return i-1


        return n*n


s = Solution()
print(s.maxContainers(n = 3, w = 5, maxWeight = 20))