class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        """"""
        pref = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                pref = pref + nums[i]
            else:
                break

        while True:
            if pref not in nums:
                return pref
            else:
                pref = pref + 1


nums = [1, 2, 3, 2, 5]
s = Solution()
print(s.missingInteger(nums))
