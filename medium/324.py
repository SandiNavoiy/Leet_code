class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort(reverse=True)
        print(nums)
        nums[1::2], nums[::2] =nums[:n//2], nums[n//2:]


        return nums
nums = [1,5,1,1,6,4]
s = Solution()
print(s.wiggleSort(nums))