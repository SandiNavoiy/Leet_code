class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ''''''


        for i in range(1,len(s)//2 + 1):
            if len(s)%i == 0:
                if s[:i]* (len(s)//i) == s:
                    return True

        return False


s = "babbabbabbabbab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))