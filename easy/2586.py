class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        """"""
        n = 0
        z = ("a", "e", "i", "o", "u")
        for i in words[left : right + 1]:
            if i[0] in z and i[-1] in z:
                n += 1
        return n


words = ["are", "Amy", "u"]
left = 0
right = 2
s = Solution()
print(s.vowelStrings(words, left, right))
