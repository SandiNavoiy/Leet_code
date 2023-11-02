class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        """максимальное количество отрицательных и положительных чисел"""
        iter_pol = 0
        iter_otr = 0
        for i in nums:
            if i > 0:
                iter_pol += 1
            elif i < 0:
                iter_otr += 1
        return max(iter_pol, iter_otr)


nums = [-2, -1, -1, 1, 2, 3]
s = Solution()
print(s.maximumCount(nums))
