import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        else:
            lena = len(str1)
            lenb = len(str2)
            gcd = math.gcd(lena, lenb)
            print(gcd)
            maxi = max(str1, str2)
            return maxi[:gcd]


str1 = "ABABAB"
str2 = "ABAB"
s = Solution()
print(s.gcdOfStrings(str1, str2))
