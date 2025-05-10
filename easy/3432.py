class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        ''' Количество разбиений с четной разностью сумм'''
        n = 0
        for i in range(1, len(nums)):

            if (sum(nums[:i]) - sum(nums[i:])) %2 == 0:
                n +=1


        return n



s = Solution()
print(s.countPartitions([10,10,3,7,6]))