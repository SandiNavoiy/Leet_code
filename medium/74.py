class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''Двоичный поиск в матрице'''
        start = 0
        fin  = len(matrix)-1
        if fin+1 == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        elif fin == 0:
            return False

        while start <= fin:

            mid  = (start + fin) // 2
            print(start)
            print(fin)
            print(mid)
            if matrix[mid][0]<= target and matrix[mid][-1]>= target:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            elif  matrix[mid][-1] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                fin = mid -1
        return False


matrix = [[1],[3]]
target =2
s = Solution()
print(s.searchMatrix(matrix, target))