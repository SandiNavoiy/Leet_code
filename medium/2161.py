class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        """ "Разделение массива в соответствии с заданным центром"""
        new_min = []
        new_max = []
        new_ser = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                new_min.append(nums[i])
            elif nums[i] > pivot:
                new_max.append(nums[i])
            elif nums[i] == pivot:
                new_ser.append(nums[i])
        return new_min + new_ser + new_max


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
# [9,5,3,10,10,12,14]
s = Solution()
print(s.pivotArray(nums, pivot))
