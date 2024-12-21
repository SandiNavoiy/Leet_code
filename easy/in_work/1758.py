class Solution:
    def minOperations(self, s: str) -> int:
        """"""
        var_1 = 0
        var_2 = 0
        for i in range(0,len(s),2):
            if s[i:i+2] != "01":
                if s[i:i+2] == "00" or s[i:i+2] == "11":
                    var_1 += 1
                else:
                    var_1 += 2
        for i in range(0, len(s), 2):
            if s[i:i + 2] != "10":
                if s[i:i + 2] == "00" or s[i:i + 2] == "11":
                    var_2 += 1
                else:
                    var_2 += 2

        print(var_1, var_2)
        return min(var_1, var_2)
s = "101101111"
sol = Solution()
print(sol.minOperations(s))