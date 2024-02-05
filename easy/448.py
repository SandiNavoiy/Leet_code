class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """Найти все числа, исчезнувшие в массиве"""
        new = []
        for i in range(1, len(nums) + 1):
            if i not in set(nums):
                new.append(i)
        return new


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDisappearedNumbers(nums))
