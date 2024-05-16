class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """"""
        rez = nums[0]
        s_max = nums[0]
        s_mins = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                s_max, s_mins = s_mins, s_max
            s_max = max(nums[i], s_max * nums[i])
            s_mins = min(nums[i], s_mins * nums[i])

            rez = max(rez, s_max)

        return rez


nums = [2, 3, -2, 4]
s = Solution()
print(s.maxProduct(nums))
