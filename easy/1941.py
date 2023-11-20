class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """"""
        x = s.count(s[0])
        print(len(s))
        print(len(set(s)))
        if len(s) / x == len(set(s)):
            return True
        elif len(set(s)) == 1:
            return True
        else:
            return False
s = "fhojjkontbncdhwxbnexplclvjyexzsvqyyhpfpnvhdskuhkuoihiqgalklqketjikdlgrawhfo"

sol = Solution()
print(sol.areOccurrencesEqual(s))