class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        lll = 0
        left = 0
        min_m = nums[0]
        max_m = nums[0]

        for right in range(len(nums)):
            if nums[right] > max_m:
                max_m = nums[right]
            if nums[right] < min_m:
                min_m = nums[right]


            while max_m - min_m > limit:

                left += 1
                min_m = min(nums[left:right + 1])
                max_m = max(nums[left:right + 1])

            lll = max(lll, right - left + 1)

        return lll

nums = [10,1,2,4,7,2]
limit = 5
s = Solution()
print(s.longestSubarray(nums, limit))