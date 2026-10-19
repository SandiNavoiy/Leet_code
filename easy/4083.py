class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        '''Минимальное количество удалений для обеспечения точности массива.'''
        n = 0
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == temp:
                n += 1
            else:
                temp = nums[i]

        return n


s = Solution()
print(s.minDeletions([1,1,2,2,2,3]))
