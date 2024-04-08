class Solution:
    def makeFancyString(self, s: str) -> str:
        ''''''
        ans = ""
        new = []
        count = 0
        for i in s:

            if ans == i:
                count += 1
                if count <= 1:
                    new.append(i)
            else:
                count = 0
                new.append(i)
            ans = i


        return "".join(new)
s = "leeetcode"
sol = Solution()
print(sol.makeFancyString(s))