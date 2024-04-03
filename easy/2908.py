class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        """"""
        sums = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j and j < k and nums[i] < nums[j] and nums[k] < nums[j]:
                        sums.append(nums[i] + nums[j] + nums[k])

        sums.sort()

        if len(sums) == 0:
            return -1
        return sums[0]


nums = [5, 4, 8, 7, 10, 2]
s = Solution()
print(s.minimumSum(nums))
