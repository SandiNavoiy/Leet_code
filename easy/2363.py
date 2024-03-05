class Solution:
    def mergeSimilarItems(
        self, items1: list[list[int]], items2: list[list[int]]
    ) -> list[list[int]]:
        """"""
        valuei = 0
        weight = 0
        ret = {}
        rr = []
        sums = items1 + items2
        sums.sort()
        for i in sums:
            if i[0] not in ret.keys():
                ret[i[0]] = i[1]
            else:
                ret[i[0]] = ret[i[0]] + i[1]
        for i, j in ret.items():
            rr.append([i, j])

        return rr


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]
s = Solution()
print(s.mergeSimilarItems(items1, items2))
