from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        """"""
        time = tasks[0][0] + tasks[0][1]
        for i in range(1, len(tasks)):
            time = min(time, tasks[i][0] + tasks[i][1])



        return time

s = Solution()
print(s.earliestTime([[1,6],[2,3]]))
