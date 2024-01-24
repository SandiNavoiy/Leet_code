class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        """"""
        nums.sort()
        count = 0
        for i in range(0, len(nums), 2):
            count += nums[i]
        return count


nums = [1, 4, 3, 2]
s = Solution()
print(s.arrayPairSum(nums))
