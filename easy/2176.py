class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        """Подсчет равных и делимых пар в массиве"""
        summ = 0
        i = 0
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i * j % k == 0:
                    summ += 1



        return summ

nums = [3,1,2,2,2,1,3]
k = 2
s = Solution()
print(s.countPairs(nums, k))
