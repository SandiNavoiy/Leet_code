class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Содержит дубликат"""
        if len(nums) == len(set(nums)):
            return False
        else:
            return True


nums = [1, 2, 3, 1]
s = Solution()
print(s.containsDuplicate(nums))
