class Solution:
    def countDigits(self, num: int) -> int:
        new_str = str(num)
        sum = 0
        for i in new_str:
            if num % int(i) == 0:
                sum = sum + 1

        return sum


num = 1248
s = Solution()
print(s.countDigits(num))
