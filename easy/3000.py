class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        ''''''
        ss = 0
        diag = 0
        for i in dimensions:
            if (i[0]* i[0] + i[1] * i[1])**0.5 > diag :
                diag = (i[0]* i[0] + i[1] * i[1])**0.5
                ss = i[0]* i[1]
            elif (i[0]* i[0] + i[1] * i[1])**0.5 == diag:
                if i[0]* i[1] > ss:
                    ss = i[0] * i[1]
        return ss

dimensions = [[9,3],[8,6]]
s = Solution()
print(s.areaOfMaxDiagonal(dimensions))
