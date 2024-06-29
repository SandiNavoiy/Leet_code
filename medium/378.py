class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        ''''''
        new = []
        for i in matrix:
            new = new + i
        new.sort()
        return new[k-1]
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
s = Solution()
print(s.kthSmallest(matrix,k))