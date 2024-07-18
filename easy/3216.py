class Solution:
    def getSmallestString(self, s: str) -> str:
        """Returns"""
        new = list(map(int, s))

        def is_ee(v):
            return v % 2 == 0

        for i in range(len(new) - 1):
            if (is_ee(new[i]) == is_ee(new[i + 1])) and (new[i + 1] < new[i]):
                new[i], new[i + 1] = new[i + 1], new[i]
                break
        rez = ""
        for i in new:
            rez = rez + str(i)

        return rez


c = "45320"
sol = Solution()
print(sol.getSmallestString(c))
