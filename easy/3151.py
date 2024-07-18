class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        """"""

        def is_t(v):
            return v % 2 == 0

        for i in range(len(nums) - 1):
            if is_t(nums[i]) == is_t(nums[i + 1]):
                return False

        return True


nums = [2, 1, 4]

s = Solution()
print(s.isArraySpecial(nums))
