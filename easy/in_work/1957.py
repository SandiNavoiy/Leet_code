class Solution:
    def makeFancyString(self, s: str) -> str:
        ''''''
        new = [x for x in s]
        new1 = []
        for i in range(len(new)-2):
            if new[i] !=  new[i+1] and new[i+2] != new[i]:
                new1.append(new[i])

        return new1
s = "leeetcode"
sol = Solution()
print(sol.makeFancyString(s))