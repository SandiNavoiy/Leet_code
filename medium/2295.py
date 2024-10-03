class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        """"""
        # решение брут
        # for i in operations:
        #    nums[nums.index(i[0])] = i[1]
        # return nums
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        for i in operations:
            temp_ind = d[i[0]]
            nums[temp_ind] = i[1]
            del d[i[0]]
            d[i[1]] = temp_ind

        return nums


nums = [1, 2, 4, 6]
operations = [[1, 3], [4, 7], [6, 1]]
s = Solution()
print(s.arrayChange(nums, operations))
