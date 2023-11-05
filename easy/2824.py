class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        """Подсчитайте пары, сумма которых меньше целевой"""
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] < target and  i < j < len(nums):
                    count += 1

        return count



nums = [-1,1,2,3,1]
target = 2
s = Solution()
print(s.countPairs(nums, target))