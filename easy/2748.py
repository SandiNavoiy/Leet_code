import math


class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        """"""
        cc = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                    cc = cc + 1

        return cc


nums = [11, 21, 12]
s = Solution()
print(s.countBeautifulPairs(nums))
