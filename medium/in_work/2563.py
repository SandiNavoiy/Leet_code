class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        """"""
        nums.sort()
        l = 0
        r = len(nums) - 1
        rez = 0
        while l < r:
            if nums[l] + nums[r] > upper:
                r = r - 1
            else:
                rez = rez + r - l
                l += 1
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] >= lower:
                r = r - 1
            else:
                rez = rez - (r - l)
                l += 1
        return rez


nums = [0, 0, 0, 0, 0, 0]
lower = 0
upper = 0
s = Solution()
print(s.countFairPairs(nums, lower, upper))
