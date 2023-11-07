class Solution:
    def finalString(self, s: str) -> str:
        """Неисправная клавиатура"""
        new_str = ""
        for i in s:
            if i != "i":
                new_str = new_str + i
            else:
                new_str = "".join(reversed(new_str))
        return new_str


s = "string"
sol = Solution()
print(sol.finalString(s))
