class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''удаление дубликатов'''
        if len(nums) < 3 :
            return len(nums)
        start = 0
        finish = 2
        while finish< len(nums):
            if nums[start] == nums[finish]:
                del nums[start]
            else:
                start = start + 1
                finish = finish + 1
        return len(nums)





nums = [1,1,1,2,2,3]
s = Solution()
print(s.removeDuplicates(nums))
