class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        """"""

        arr1 = min(nums)
        nums.pop(nums.index(arr1))
        print(nums)
        arr2 = min(nums)
        nums.pop(nums.index(arr2))
        print(nums)
        arr3 = nums[0]
        print(nums)

        return arr1 + arr2 + arr3
nums = [1,6,1,5]
s = Solution()
print(s.minimumCost(nums))