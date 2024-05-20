class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        """"""
        rez = []
        x = sorted(intervals + [newInterval])
        for i, j in x:
            if rez and i <= rez[-1][-1]:
                rez[-1][-1] = max(rez[-1][-1], j)
            else:
                rez.append([i, j])

        return rez


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [2, 5]
s = Solution()
print(s.insert(intervals, newInterval))
