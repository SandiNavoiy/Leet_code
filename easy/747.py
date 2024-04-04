class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        """"""
        index_max = 0
        mmax = 0
        for i in range(len(nums)):
            if nums[i] > mmax:
                mmax = nums[i]
                index_max = i

        for i in range(len(nums)):
            if nums[i] * 2 > mmax and i != index_max:
                return -1

        return index_max


nums = [3, 6, 1, 0]
s = Solution()
print(s.dominantIndex(nums))
