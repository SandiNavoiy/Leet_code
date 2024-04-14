class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        ''''''
        new_s = s[::-1]
        for i in range(0,len(s)-1):

            if s[i:i+2] in new_s:
                print(s[i:i+2])
                return True


        return False

s = "abcd"
sol = Solution()
print(sol.isSubstringPresent(s))