class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        """Количество различных средних значений"""
        nums.sort()
        unique_averages = set()
        while len(nums) > 1:
            unique_averages.add((nums.pop(-1) + nums.pop(0)) / 2)
        return len(set(unique_averages))


nums = [4, 1, 4, 0, 3, 5]
s = Solution()
print(s.distinctAverages(nums))
