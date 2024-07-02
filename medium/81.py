class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """Search"""
        if target in nums:
            return True
        else:
            return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
s = Solution()
print(s.search(nums, target))
