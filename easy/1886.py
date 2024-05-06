
import numpy as np

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        ''''''
        for _ in range(4):
            mat = np.rot90(mat)
            if np.allclose (mat, target):
                return True
        return False


mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
s = Solution()
print(s.findRotation(mat, target))