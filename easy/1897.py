class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        """"""
        new = ""
        counts = len(words)

        if counts <= 1:
            return True
        for i in words:
            new += i

        for i in set(new):
            if new.count(i) % counts != 0:
                return False
        return True


words = [
    "caaaaa",
    "aaaaaaaaa",
    "a",
    "bbb",
    "bbbbbbbbb",
    "bbb",
    "cc",
    "cccccccccccc",
    "ccccccc",
    "ccccccc",
    "cc",
    "cccc",
    "c",
    "cccccccc",
    "c",
]


s = Solution()
print(s.makeEqual(words))
