class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """Отсутствует номер"""
        n = len(nums)
        for i in range(n + 1):
            if i not in nums:
                return i


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

s = Solution()
print(s.missingNumber(nums))
