from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        output = []

        while len(nums):
            output.append(list(set(nums)))

            for i in output[-1]:
                nums.pop(nums.index(i))

        return output


nums = [1, 3, 4, 1, 2, 3, 1]
s = Solution()
print(s.findMatrix(nums))
# [[1,3,4,2],[1,3],[1]]
