class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        """"""
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            if i == 0:
                arr1.append(nums[0])
            elif i == 1:
                arr2.append(nums[1])
            elif arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            elif arr1[-1] < arr2[-1]:
                arr2.append(nums[i])

        return arr1 + arr2


nums = [1, 2, 14, 15]
s = Solution()
print(s.resultArray(nums))
# [1, 2, 14,15 ]
