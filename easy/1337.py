class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        ''''''
        new = []

        for i in range(len(mat)):
            new.append([i, mat[i].count(1)])
        new.sort(key=lambda x: x[1])
        arr = [new[x][0] for x in range(k)]

        return arr

mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
s = Solution()
print(s.kWeakestRows(mat, k))