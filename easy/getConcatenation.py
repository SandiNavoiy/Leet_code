class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """удваение списка"""

        nums_new = nums * 2
        return nums_new


nums = [1, 3, 2, 1]

sol = Solution()

print(sol.getConcatenation(nums))
