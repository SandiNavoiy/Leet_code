class Solution:
    """Перестановка массива по индексу"""

    __slots__ = ["nums"]

    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans


nums = [0, 2, 1, 5, 3, 4]
s = Solution()
print(s.buildArray(nums))

# [0,1,2,4,5,3]
