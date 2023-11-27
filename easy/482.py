class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """"""
        while "-" in s:
            s = s.replace("-", "")
        s = s[::-1]
        new = ''
        print(s)

        for i in range(len(s)):


            if (int(i)) % k == 0 and int(i) != 0:
                new =  new + '-'
            new = new + s[i]
        return new[::-1].upper()

s = "5F3Z-2e-9-w"
k = 3

sol = Solution()
print(sol.licenseKeyFormatting(s, k))
