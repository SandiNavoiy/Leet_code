class Solution:
    def sortVowels(self, s: str) -> str:
        """"""
        x = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        new = []
        for i in s:
            if i in x:
                new.append(i)
        new.sort()
        ne = 0
        new_s = list(s)
        for i in range(len(new_s)):
            if new_s[i] in x:
                new_s[i] = new[ne]
                ne += 1

        return "".join(new_s)


s = "lEetcOde"
sol = Solution()
print(sol.sortVowels(s))
