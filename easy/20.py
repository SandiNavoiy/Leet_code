class Solution:
    def isValid(self, s: str) -> bool:
        """"""
        stack = list(s)
        new = []
        for i in stack:
            if i == "(" or i == "{" or i == "[":
                new.append(i)
            elif i == ")" and new and new[-1] == "(":
                new.pop()

            elif i == "]" and new and new[-1] == "[":
                new.pop()
            elif i == "}" and new and new[-1] == "{":
                new.pop()
            else:
                return False
        return len(new) == 0


s = "()"
sol = Solution()
print(sol.isValid(s))
