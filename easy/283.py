class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        # Перемещаем ненулевые элементы в начало списка
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1


nums = [0, 0, 1]
# 1,0,0]

s = Solution()
print(s.moveZeroes(nums))
