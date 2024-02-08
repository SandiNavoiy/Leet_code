class Solution:
    def countKeyChanges(self, s: str) -> int:
        """"""
        new = s.lower()
        index = 0
        for i in range(1, len(new)):
            if new[i] != new[i - 1]:
                index += 1
        return index


s = "aAbBcC"
sol = Solution()
print(sol.countKeyChanges(s))
