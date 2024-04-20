class Solution:
    def reverseWords(self, s: str) -> str:
        ''''''


        new = [i for i in s.split(' ') if i != ""]

        x = new[::-1]

        return " ".join(x)
s = "  hello world  "
sol = Solution()
print(sol.reverseWords(s))