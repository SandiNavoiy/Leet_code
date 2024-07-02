class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """"""
        if target not in nums:
            return -1

        return nums.index(target)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
s = Solution()
print(s.search(nums, target))
