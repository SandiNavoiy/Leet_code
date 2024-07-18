class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        """"""
        new = s * (k + 2)
        rez = ""
        for i in range(len(s)):
            rez = rez + new[i + k]

        return rez


s = "aaa"
k = 1
sol = Solution()
print(sol.getEncryptedString(s, k))
