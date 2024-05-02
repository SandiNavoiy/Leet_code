class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """"""

        if target in nums:
            return nums.index(target)

        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
s = Solution()
print(s.search(nums, target))
