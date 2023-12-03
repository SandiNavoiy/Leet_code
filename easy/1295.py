class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """Найти числа с четным количеством цифр"""
        n  = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                n += 1
        return n

nums = [12,345,2,6,7896]
s = Solution()
print(s.findNumbers(nums))