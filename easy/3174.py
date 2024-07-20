class Solution:
    def clearDigits(self, s: str) -> str:
        """"""
        new = list(s)
        rez = []
        for i in new:
            if not i.isdigit():
                rez.append(i)
            else:
                rez.pop()

        return "".join(rez)


s = "abc12"
sol = Solution()
print(sol.clearDigits(s))
