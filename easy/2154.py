class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        """Продолжайте умножать найденные значения на два"""
        nums.sort()
        if original not in nums:
            return original
        else:
            for j in nums:
                if j == original:
                    original = original * 2

            return original


nums = [8, 19, 4, 2, 15, 3]
original = 2
s = Solution()
print(s.findFinalValue(nums, original))
