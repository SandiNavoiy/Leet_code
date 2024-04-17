class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """"""
        new = []
        x = len(nums)
        for i in range(x):
            for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                if nums[j] == key:
                    if i not in new:
                        new.append(i)
        return new


nums = [2, 2, 2, 2, 2]
key = 2
k = 2
s = Solution()
print(s.findKDistantIndices(nums, key, k))
