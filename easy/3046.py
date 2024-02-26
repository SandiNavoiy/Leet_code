class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        """"""
        ss = int(sum(nums) / 2)
        for i in nums:
            if nums.count(i) > 2:
                return False
        return True


nums = [1, 1, 2, 2, 3, 4]
s = Solution()
print(s.isPossibleToSplit(nums))
