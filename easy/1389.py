class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """Создайте целевой массив в заданном порядке"""
        new = []
        for i in range(len(index)):
            new.insert(index[i], nums[i])

        return new


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

s = Solution()
print(s.createTargetArray(nums, index))
