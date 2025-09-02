from sys import prefix


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        '''Максимальная абсолютная сумма'''
        max_sum = 0
        min_sum = 0
    #префиксная сумма
        prefix_sum=0
        for i in nums:
            prefix_sum = prefix_sum + i
            max_sum = max(max_sum,prefix_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum - min_sum

s = Solution()
print(s.maxAbsoluteSum([1,-3,2,3,-4]))