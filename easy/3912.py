class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        '''Допустимые элементы в массиве'''
        if len(nums) == 1:
            return nums
        rez = [nums[0]]
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        left_max[0] = nums[0]
        right_max[-1] = nums[-1]
        for i in range(1, len(nums)):
            left_max[i] = max(left_max[i-1], nums[i])
        for i in range(len(nums)-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])

        for i in range(1, len(nums)-1):
            if nums[i] > left_max[i-1] or nums[i] > right_max[i+1]:
                rez.append(nums[i])
        rez.append(nums[-1])
        return rez



s = Solution()
print(s.findValidElements([1,2,4,2,3,2]))