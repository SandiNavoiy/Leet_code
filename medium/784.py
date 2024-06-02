from itertools import product


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        """"""
        new = []
        for ch in s:
            new.append([ch] if ch.isdigit() else [ch.lower(), ch.upper()])
        print(new)

        return ["".join(v) for v in product(*new)]


s = "a1b2"
sol = Solution()
print(sol.letterCasePermutation(s))
