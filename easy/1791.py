class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        """Найти центр звездного графика"""
        new = []
        res = 0
        for i in edges:
            for j in i:
                new.append(j)
        for i in new:
            if new.count(i) > 1:
                res = i

        return res


edges = [[1, 2], [2, 3], [4, 2]]
s = Solution()
print(s.findCenter(edges))
