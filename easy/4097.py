class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        '''Минимальное значение объединенных целых чисел'''
        rez = []

        for i in range(0, len(nums)-1, 2):
            rez.append(int(str(nums[i]) + str(nums[i+1])))


        return min(rez)




s = Solution()
print(s.minMergedInteger([23,55,42,21]))
