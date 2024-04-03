class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        """"""
        d = {}
        for i in range(len(nums) - 1):
            ss = nums[i] + nums[i + 1]
            if ss not in d.keys():
                d[ss] = [nums[i], nums[i + 1]]
            else:
                return True

        return False


nums = [1, 2, 3, 4, 5]
s = Solution()
print(s.findSubarrays(nums))
