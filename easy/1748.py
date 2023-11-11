class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        """
        Сумма уникальных элементов

        """
        new = []
        for i in nums:
            if nums.count(i) == 1:
                new.append(i)
        return sum(new)


nums = [1, 2, 3, 2]

s = Solution()
print(s.sumOfUnique(nums))
