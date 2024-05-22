class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ''''''
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j>= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17, 24],[18,21,23,26,30]]
target = 5
s = Solution()
print(s.searchMatrix(matrix,target))