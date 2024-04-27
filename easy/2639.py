class Solution:
    def findColumnWidth(self, matrix: List[List[int]]) -> List[int]:
        result = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j] = max(result[j], len(str(matrix[i][j])))
        return result
