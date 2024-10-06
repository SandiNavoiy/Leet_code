class Solution:
    def stringHash(self, s: str, k: int) -> str:
        """"""
        result = ""
        for i in range(0, len(s), k):
            temp = 0
            for j in s[i : i + k]:
                temp = temp + ord(j) - 97
            new = chr(temp % 26 + 97)
            result += new

        return result


s = "abcd"
k = 2
sol = Solution()
print(sol.stringHash(s, k))
