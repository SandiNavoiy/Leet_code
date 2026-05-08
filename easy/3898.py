class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ''''''
        ls = []

        for i in range(len(matrix)):
            ls.append(sum(matrix[i]))
        return ls


s = Solution()
print(s.findDegrees([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))