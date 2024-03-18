class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        """"""
        new = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        new += 1
        return new


nums = [4, 4, 2, 4, 3]
s = Solution()
print(s.unequalTriplets(nums))
