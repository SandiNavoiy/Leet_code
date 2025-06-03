class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """"""

        rez = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if nums[i:j].count(0) <= 1:
                    rez = max(rez, len(nums[i:j]) - 1)
                else:
                    break
        return rez


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]


s = Solution()
print(s.longestSubarray(nums))
