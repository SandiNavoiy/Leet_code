from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        ''''''
        temp = defaultdict(list)
        rez = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp[i+j].append(mat[i][j])

        for index, val in temp.items():
            if index % 2 == 0:
                rez.extend(val[::-1])
            else:
                rez.extend(val)
        print(rez)
        return rez
mat = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.findDiagonalOrder(mat))
#[1,2,4,7,5,3,6,8,9]