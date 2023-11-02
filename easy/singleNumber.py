class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """ "Единый номер"""
        n = 0
        for i in nums:
            if nums.count(i) == 1:
                n = i

        return n


nums = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))
