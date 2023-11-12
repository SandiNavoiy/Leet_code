class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        return s


s = ["h", "e", "l", "l", "o"]
sol = Solution()
print(sol.reverseString(s))
