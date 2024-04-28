from collections import Counter

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        mmm = max(nums)
        new = 0
        counter = Counter()
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and counter[mmm] < k:
                counter[nums[j]] += 1
                j += 1
            if counter[mmm] >= k:
                new += len(nums) - j + 1
            counter[nums[i]] -= 1
        return new
nums = [1,3,2,3,3]
k = 2
s = Solution()
print(s.countSubarrays(nums, k))