class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """Сортировка массива по четности"""
        new1 = []
        new2 = []
        for i in nums:
            if i % 2 == 0:
                new1.append(i)
            else:
                new2.append(i)
        return new1 + new2


nums = [3, 1, 2, 4]
s = Solution()
print(s.sortArrayByParity(nums))
