class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ''''''
        new = []
        for i in target:
            new.append([s.count(i), target.count(i)])

        return new
s = "abbaccaddaeea"
target = "aaaaa"
sol = Solution()
print(sol.rearrangeCharacters(s, target))