class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        """Минимальное количество свопов для перемещения нулей к концу."""
        nums = [0 if i == 0 else 1 for i in nums]
        c = nums.count(0)


        return c - nums[-1*c:].count(0)


s = Solution()
print(s.minimumSwaps(nums = [0,1,0,2]))