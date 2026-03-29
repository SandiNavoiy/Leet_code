from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        """"""
        s = dict(Counter(nums))

        rez = 0
        for num in nums:

            if s[num] % k == 0:
                rez += num


        return rez



s = Solution()
print(s.sumDivisibleByK([1,2,2,3,3,3,3,4], 2))
