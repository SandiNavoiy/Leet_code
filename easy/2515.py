class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        """"""
        if target not in words:
            return -1
        a = []
        for i in range(startIndex, len(words)):
            if words[i] == target:
                a.append(abs(i - startIndex))
                a.append((len(words) - i + startIndex))
        for i in range(startIndex - 1, -1, -1):
            if words[i] == target:
                a.append(abs(i - startIndex))
                a.append((len(words) - startIndex + i))

        return min(a)


words = [
    "hsdqinnoha",
    "mqhskgeqzr",
    "zemkwvqrww",
    "zemkwvqrww",
    "daljcrktje",
    "fghofclnwp",
    "djwdworyka",
    "cxfpybanhd",
    "fghofclnwp",
    "fghofclnwp",
]
target = "zemkwvqrww"
startIndex = 8
s = Solution()
print(s.closetTarget(words, target, startIndex))
