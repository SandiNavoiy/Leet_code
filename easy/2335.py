class Solution:
    def fillCups(self, amount: list[int]) -> int:
        """"""
        t = 0
        amount.sort()
        if sum(amount) == 0:
            return t

        while True:
            if amount[2] > 0:
                amount[2] = amount[2] - 1
            if amount[1] > 0:
                amount[1] = amount[1] - 1
            amount.sort()
            t = t + 1
            if sum(amount) == 0:
                break

        return t


amount = [1, 4, 2]
s = Solution()
print(s.fillCups(amount))
