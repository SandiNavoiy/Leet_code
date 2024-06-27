class Solution:
    def minimumChairs(self, s: str) -> int:
        """"""
        rez = 0
        temp = 0
        for i in s:
            if i == "E":
                temp = temp + 1
                rez = max(rez, temp)
            else:
                temp = temp - 1

        return rez


s = "ELEELEELLL"
sol = Solution()
print(sol.minimumChairs(s))
