class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        """"""
        rez = []
        new = text.split()
        for i in range(len(new) - 2):
            if new[i] == first and new[i + 1] == second:
                rez.append(new[i + 2])

        return rez


text = "alice is a good girl she is a good student"
first = "a"
second = "good"
s = Solution()
print(s.findOcurrences(text, first, second))
