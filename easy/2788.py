class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        """"""
        new = []
        for i in words:
            if separator in i:
                x = i.split(separator)
                new.extend(x)
            else:
                new.append(i)
        while "" in new:
            new.remove("")
        return new


words = ["$easy$", "$problem$"]
separator = "$"
# ["one","two","three","four","five","six"]
s = Solution()
print(s.splitWordsBySeparator(words, separator))
