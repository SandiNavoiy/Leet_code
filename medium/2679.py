class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        """"""
        new = nums[0]
        for i in nums:
            i.sort(reverse=True)
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                new[j] = max(new[j], nums[i][j])
        return sum(new)


nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
s = Solution()
print(s.matrixSum(nums))
