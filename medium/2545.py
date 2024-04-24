class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        ''''''
        score.sort(key= lambda x: x[k], reverse=True)

        return score
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
s = Solution()
print(s.sortTheStudents(score,k))