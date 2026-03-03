from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        """"""
        ls = []
        for i in range(1,len(cost)+1):
            ls.append(min(cost[:i]))


        return ls



s = Solution()
print(s.minCosts([5,3,4,1,3,2]))
