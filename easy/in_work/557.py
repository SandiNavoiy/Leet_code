class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        new_add = []
        for i in s:
            new_add.append(i[::-1])

        return " ".join(new_add)


s = "Let's take LeetCode contest"
sol = Solution()
print(sol.reverseWords(s))
