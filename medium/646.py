class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """"""
        new = []

        pairs.sort(key=lambda x: x[1])
        new.append(pairs[0])

        for i in range(1, len(pairs)):
            if pairs[i][0] > new[-1][1]:
                new.append(pairs[i])
        return len(new)


pairs = [[1, 2], [2, 3], [3, 4]]
s = Solution()
print(s.findLongestChain(pairs))
