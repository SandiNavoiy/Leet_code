from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ''''Максимизация силы пары с использованием НОД'''

        rez = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                rez = max(rez, (nums[i]* nums[j] / (gcd(nums[i], nums[j]))**2))


        return int(rez)



s = Solution()
print(s.maxPairStrength([2,3,5]))
