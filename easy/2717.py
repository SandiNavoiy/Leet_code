class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        ''''''
        n = len(nums)
        x = nums.index(1)
        y = nums.index(n)

        if x < y:
            return x + (n - y - 1)
        else:
            return x + (n - y - 1) - 1
        return x
s = Solution()
nums = [2,1,4,3]
print(s.semiOrderedPermutation(nums))