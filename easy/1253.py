class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        """"""
        new = [[0 for i in range(n)] for j in range(m)]

        for i in indices:
            for j in range(len(new[i[0]])):
                new[i[0]][j] = new[i[0]][j] + 1
            if len(new) > 1:
                for k in range(len(new)):
                    new[k][i[1]] = new[k][i[1]] + 1

        ss = 0
        for i in new:
            for j in i:
                if j % 2 != 0:
                    ss += 1

        return ss


m = 48
n = 37
indices = [[40, 5]]
s = Solution()
print(s.oddCells(m, n, indices))
