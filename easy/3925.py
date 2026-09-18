class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        """Объединение массива с обратным порядком."""


        return nums + nums[::-1]




n = [1,2,3]

s = Solution()
print(s.concatWithReverse(n))
