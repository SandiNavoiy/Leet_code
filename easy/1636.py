import collections
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counts_dict = collections.Counter(nums)
        return sorted(nums, key = lambda x: (counts_dict[x], -x))
nums = [1,1,2,2,2,3]
#[3,1,1,2,2,2]
s = Solution()
print(s.frequencySort(nums))