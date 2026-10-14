class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        '''Уникальный средний элемент'''

        l = len(nums)//2

        return nums.count(nums[l]) == 1

s = Solution()
print(s.isMiddleElementUnique([1,2,2]))