from itertools import combinations


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """"""
        glass = ("a", "e", "i", "o", "u")
        new = list(combinations(glass, n))
        if n > 1:
            return len(new) + 5 * (n - 1)
        return len(new)


n = 33
s = Solution()
print(s.countVowelStrings(n))
