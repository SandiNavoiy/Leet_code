class Solution:
    def removeStars(self, s: str) -> str:
        """Удаление звездочек из строки"""
        new = list(s)
        b = []

        for i in new:
            if i == "*":
                b.pop()
            else:
                b.append(i)

        return "".join(b)


s = "leet**cod*e"

sol = Solution()
print(sol.removeStars(s))
