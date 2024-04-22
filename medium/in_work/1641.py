from itertools import combinations


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """"""
        glass = ("a", "e", "i", "o", "u")
        new = list(combinations(glass, n))
        print(new)


n = 2
s = Solution()
print(s.countVowelStrings(n))
