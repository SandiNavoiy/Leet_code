from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        ''''''
        rez  = [0] * k
        x = defaultdict(list)
        y= defaultdict(int)
        for i in logs:
            if i[1] not in x[i[0]]:
                x[i[0]].append(i[1])
                y[i[0]]  = y[i[0]] + 1
        for val in y.values():
            rez[val-1] = rez[val-1] + 1
        return rez
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
s = Solution()
print(s.findingUsersActiveMinutes(logs, k))