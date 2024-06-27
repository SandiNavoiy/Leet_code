class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        """"""
        max_len = 0
        temp = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                temp = temp + 1
            else:
                max_len = max(max_len, temp)
                temp = 0
        max_len = max(max_len, temp)
        return max_len + 1


nums = [1, 3, 5, 7]
s = Solution()
print(s.findLengthOfLCIS(nums))
