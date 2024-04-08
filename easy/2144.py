class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        """"""
        sss = 0
        cost.sort()
        if len(cost) <= 2:
            return sum(cost)
        while len(cost) > 0:
            sss += cost.pop(-1)
            if len(cost) == 0:
                break
            sss += cost.pop(-1)
            if len(cost) == 0:
                break
            cost.pop(-1)
        return sss


cost = [3, 3, 3, 1]
s = Solution()
print(s.minimumCost(cost))
