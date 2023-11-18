class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """ . Поиск позиции вставки"""
        n = 0
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    n = i
            return  n
        elif nums[-1] < target:
            n = len(nums)
            return n
        else:
            for j in range(len(nums)):
                if nums[j] > target:

                    n = j
                    return n

nums = [1,3,5,6]
target = 7

s = Solution()
print(s.searchInsert(nums, target))
