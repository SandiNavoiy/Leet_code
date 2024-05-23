class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''''''
        s = s.lower()
        new = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                new = new + i
        return new == new[::-1]
s = "0P"
sol = Solution()
print(sol.isPalindrome(s))