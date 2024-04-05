class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        ''''''
        ii = -1
        jj = -1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    ii = i
                    jj = j
                    break

        if ii == -1 and jj == -1:
            return [-1, -1]
        return [ii, jj]

nums = [0]
indexDifference = 0
valueDifference = 0
s = Solution()
print(s.findIndices(nums, indexDifference, valueDifference))