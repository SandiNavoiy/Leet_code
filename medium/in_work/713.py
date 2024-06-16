from functools import reduce


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """"""
        rez = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if reduce(lambda a, b: a * b, nums[i:j]) < k:
                    rez.append(nums[i:j])
                else:
                    break
        return len(rez)


nums = [10, 5, 2, 6]
k = 100
s = Solution()
print(s.numSubarrayProductLessThanK(nums, k))
