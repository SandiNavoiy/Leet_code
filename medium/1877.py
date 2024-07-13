class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """"""
        nums.sort()
        new1 = nums[: int(len(nums) / 2)]
        new2 = nums[int(len(nums) / 2) :][::-1]
        rez = 0
        for i, j in zip(new1, new2):
            rez = max(rez, i + j)
        return rez


nums = [3, 5, 4, 2, 4, 6]
s = Solution()
print(s.minPairSum(nums))
