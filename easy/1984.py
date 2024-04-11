class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        """"""
        nums.sort()

        sss = nums[k - 1] - nums[0]
        for i in range(1, len(nums) - k + 1):
            if nums[i + k - 1] - nums[i] < sss:
                sss = nums[i + k - 1] - nums[i]

        return sss


nums = [9, 4, 1, 7]
k = 2
s = Solution()
print(s.minimumDifference(nums, k))
