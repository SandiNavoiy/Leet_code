class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """Разделение струны в сбалансированных струнах"""
        r_val = []
        l_val = []
        ans = 0
        for i in s:

            if i == "R":
                r_val.append("R")

            if i == "L":
                l_val.append("L")

            if (len(r_val) == len(l_val)) and (len(r_val) != 0 and len(l_val) != 0):
                r_val.clear()
                l_val.clear()
                ans += 1

        return (ans)


s = 'RLRRLLRLRL'
sol = Solution()
print(sol.balancedStringSplit(s))
