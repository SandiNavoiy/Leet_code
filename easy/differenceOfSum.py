class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        """Разница между суммой элементов и суммой цифр массива"""
        summ  = sum(nums)
        summ1 = 0
        listToStr = ''.join(map(str, nums))
        for i in listToStr:
            summ1 = int(i) + summ1


        return abs(summ - summ1)






nums = [1,15,6,3]
s = Solution()
print(s.differenceOfSum(nums))
