class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        """Переставьте строки, чтобы избежать пар символов."""
        yyy = ""
        xxx = ""
        ost = ""
        for i in s:
            if i == x:
                xxx = xxx +i
            elif i == y:
                yyy = yyy +i
            else:
                ost = ost +i
        return yyy + ost + xxx



sol = Solution()
print(sol.rearrangeString("aabc", x="a", y="c"))