class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """"""
        new = []
        for i in s:
            if i not in new:
                new.append(i)
            else:
                return i


s = "abccbaacz"
sol = Solution()
print(sol.repeatedCharacter(s))
