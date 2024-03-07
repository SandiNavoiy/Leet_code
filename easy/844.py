class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """"""
        new1 = []
        new2 = []
        for i in s:
            if i != "#":
                new1.append(i)
            else:
                if len(new1) >= 1:
                    new1.pop(-1)

        for i in t:
            if i != "#":
                new2.append(i)
            else:
                if len(new2) >= 1:
                    new2.pop(-1)

        if new1 != new2:
            return False
        return True


s = "ab##"
t = "c#d#"
sol = Solution()
print(sol.backspaceCompare(s, t))
