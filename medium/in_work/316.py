from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """"""

        x = dict(Counter(s))
        new_s = list(s)
        rez = []
        for i in new_s:
            if x[i] == 1:
                rez.append(i)
            else:
                x[i] = x[i] - 1
        print(rez)

        return "".join(rez)


s = "cbacdcbc"
sol = Solution()
print(sol.removeDuplicateLetters(s))
# acdb
