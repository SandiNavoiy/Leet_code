class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> list[list[int]]:
        """"""
        new = [[x, y] for x in range(rows) for y in range(cols)]
        new.sort(key=lambda point: abs(point[0] - rCenter) + abs(point[1] - cCenter))
        return new


rows = 1
cols = 2
rCenter = 0
cCenter = 0
s = Solution()
print(s.allCellsDistOrder(rows, cols, rCenter, cCenter))
