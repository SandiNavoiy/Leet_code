class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        """Ни минимум, ни максимум"""
        new = sorted(set(nums))
        v = 0
        if len(new) <= 2:
            v = -1
        else:
            v = new[1]

        return v


nums = [3, 2, 1, 4]

s = Solution()
print(s.findNonMinOrMax(nums))
