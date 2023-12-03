class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """"""
        nums.sort()
        n = []

        for i in range(len(nums)):
            if nums[i] == target:
                n.append(i)
        return n
nums = [1,2,5,2,3]
target = 3

s = Solution()
print(s.targetIndices(nums, target))