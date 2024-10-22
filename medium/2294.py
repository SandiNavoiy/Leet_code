class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        """"""
        nums.sort()
        if k == 0:
            return len(set(nums))
        if nums[-1] - nums[0] <= k:
            return 1
        v = 0
        temp = nums[0]

        for i in range(len(nums)):
            if nums[i] - temp > k:
                temp = nums[i]
                v = v + 1

        return v + 1


nums = [3, 6, 1, 2, 5]
k = 2
s = Solution()
print(s.partitionArray(nums, k))
