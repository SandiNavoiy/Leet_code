class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums):
            nums = nums
        elif k < len(nums):
            nums = nums[len(nums) - k :] + nums[: len(nums) - k]
        else:
            k = int(k / len(nums))
            nums = nums[len(nums) - k :] + nums[: len(nums) - k]

        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
print(s.rotate(nums, k))
