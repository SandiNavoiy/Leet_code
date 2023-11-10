class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """"Текущая сумма 1d массива"""
        sum = 0
        sums = []
        for i in nums:
            sum = sum + i
            sums.append(sum)
        return sums

nums = [1,2,3,4]
s = Solution()
print(s.runningSum(nums))