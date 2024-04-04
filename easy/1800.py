class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = 0

        curr = nums[0]
        for i, n in enumerate(nums[1:]):
            if n <= nums[i]:
                res = max(res, curr)
                curr = n
            else:
                curr += n

        return max(res, curr)


nums = [10, 20, 30, 5, 10, 50]
s = Solution()
print(s.maxAscendingSum(nums))
