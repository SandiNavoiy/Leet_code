class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        """Наибольшее целое число, сумма цифр которого равна заданному числу."""
        rez = -1

        for i in range((10**(n)-1), -1, -1):


            if sum([int(j) for j in str(i)]) == s:

                rez = i
                break
        return rez

n = 5
s = 0
e = Solution()
print(e.largestInteger(n, s))