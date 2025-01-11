
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        ''''''
        rez = [[0,0] for i in range(n+1)]

        for i in trust:
            rez[i[0]][0] += 1
            rez[i[1]][1] += 1

        for i in range(len(rez)):
            if rez[i][0] == 0 and rez[i][1] == n-1:

                return i
        return -1

n = 3
trust = [[1,3],[2,3]]
s = Solution()
print(s.findJudge(n, trust))