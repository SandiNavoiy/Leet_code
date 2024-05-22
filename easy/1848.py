class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        """"""
        x = []
        for i in range(len(nums)):
            if nums[i] == target:
                x.append(abs(i - start))

        return min(x)


nums = [2202, 9326, 1034, 4180, 1932, 8118, 7365, 7738, 6220, 3440]
target = 3440
start = 0
s = Solution()
print(s.getMinDistance(nums, target, start))
