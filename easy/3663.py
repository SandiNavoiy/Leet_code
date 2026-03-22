class Solution:
    def largestEven(self, s: str) -> str:
        """Напишите функцию, которая принимает строку и возвращает наибольшее четное число, которое можно получить из цифр строки."""

        if s[-1] == "2":
            return s

        else:
            inx  = len(s) - 1
            while inx >= 0:
                if s[inx] == "2":
                    return s[:inx] + "2"
                inx -= 1

        return ""


s = Solution()
print(s.largestEven("111"))
