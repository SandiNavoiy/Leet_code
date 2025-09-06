class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """"""
        rez = 0
        start = 0
        for end in range(len(nums)):
            rez = max(rez, end - start + 1)



        return rez



nums = [1,1,1,0]


s = Solution()
print(s.longestSubarray(nums))
