class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """Квадраты отсортированного массива"""
        new = []
        for i in nums:
            new.append(i * i)
        new.sort()
        return new


nums = [-4, -1, 0, 3, 10]
s = Solution()
print(s.sortedSquares(nums))
