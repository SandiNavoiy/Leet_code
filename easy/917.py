class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """"""
        new = [x for x in s if x.isalpha()]
        new.reverse()

        for i in range(len(s)):
            if s[i].isalpha() == False:
                new.insert(i, s[i])

        return "".join(new)


s = "ab-cd"
sol = Solution()
print(sol.reverseOnlyLetters(s))
# Qedo1ct-eeLg=ntse-T!
