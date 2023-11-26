class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """Максимальное среднее подмассив I"""
        nums.sort(key=abs, reverse=True)

        l = sum(nums[0:k]) / k
        return l


nums = [1, 0, 1, 4, 2]
k = 4
s = Solution()
print(s.findMaxAverage(nums, k))
