class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        """Максимальная разница между соседними элементами в круговой решетке"""
        maxx = 0
        for i in range(len(nums) - 1):
            maxx = max(maxx, abs(nums[i] - nums[i + 1]))

        return max(maxx, abs(nums[0] - nums[-1]))


s = Solution()
print(s.maxAdjacentDistance([-5, -10, -5]))
