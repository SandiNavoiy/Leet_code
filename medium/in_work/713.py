class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """"""
        if k <= 1:
            return 0
        left = 0
        proizv = 1
        count = 0
        for right in range(len(nums)):
            proizv = proizv * nums[right]
            while proizv >= k and left <= right:
                proizv = proizv // nums[left]
                left = left + 1
            count = count + right - left + 1

        return count


nums = [10, 5, 2, 6]
k = 100
s = Solution()
print(s.numSubarrayProductLessThanK(nums, k))
