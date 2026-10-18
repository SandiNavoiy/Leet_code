class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        '''Минимальное количество удалений для обеспечения точности массива.'''
        return len(set(nums))


s = Solution()
print(s.minDeletions([1,1,2,2,2,3]))
