from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """"""

        x = dict(Counter(s))
        rez = []
        visid = set()
        for i in s:
            x[i] = x[i] - 1
            if i in visid:
                continue
            while rez and i < rez[-1] and x[rez[-1]] > 0:
                visid.remove(rez.pop())
            visid.add(i)
            rez.append(i)
            print(visid)
            print(rez)

        return "".join(rez)


s = "cbacdcbc"
sol = Solution()
print(sol.removeDuplicateLetters(s))
# acdb
