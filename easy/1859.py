class Solution:
    def sortSentence(self, s: str) -> str:
        """"""

        w = s[::-1].split(" ")
        w.sort()
        new = []
        for i in w:
            i = i[::-1]
            new.append(i[:-1:])

        return " ".join(new)


s = "is2 sentence4 This1 a3"
sol = Solution()
print(sol.sortSentence(s))
