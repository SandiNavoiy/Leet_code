class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        """Лексикографически наименьший палиндром"""
        new_str = ""
        if s == s[::-1]:
            return str(s)
        n = int(len(s))
        if n % 2 == 0:
            new_str = s[0 : int(n / 2)] + s[int((n - 1) / 2) :: -1]
            return new_str
        if n % 2 != 0:
            new_str = s[0 : int(n / 2)] + s[int((n - 1) / 2) :: -1]
            return new_str


s = "egcfe"
sol = Solution()
print(sol.makeSmallestPalindrome(s))
