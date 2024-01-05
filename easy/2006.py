class Solution:
    def countKDifference(self, nums, k):
        c, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(nums[i] - nums[j]) == k:
                    c += 1
        return c


nums = [1, 2, 2, 1]
k = 1
s = Solution()
print(s.countKDifference(nums, k))
