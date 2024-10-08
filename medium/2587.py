class Solution:
    def maxScore(self, nums: list[int]) -> int:
        """"""
        nums.sort(reverse=True)
        ans = 0
        for i, n in enumerate(nums):
            ans = ans + n
            if ans <= 0:
                return i

        return len(nums)


nums = [-2, -3, 0]
s = Solution()
print(s.maxScore(nums))
