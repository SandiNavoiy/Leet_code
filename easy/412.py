class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """Физз Базз"""
        nwe = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                nwe.append("FizzBuzz")
            elif i % 3 == 0:
                nwe.append("Fizz")
            elif i % 5 == 0:
                nwe.append("Buzz")
            else:
                nwe.append(str(i))
        return nwe


n = 15

s = Solution()
print(s.fizzBuzz(n))
