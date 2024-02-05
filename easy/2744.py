class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        """"""
        x = 0
        for i in words:
            for j in words:
                if i == j[::-1] and i != j:
                    print(i)

                    x += 1
        return int(x / 2)


words = ["ff", "tx", "qr", "zw", "wr", "jr", "zt", "jk", "sq", "xx"]
s = Solution()
print(s.maximumNumberOfStringPairs(words))
