class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """"""
        rez = 0
        intervals.sort(key=lambda x: x[1])
        pref = intervals[0]

        for i in range(1, len(intervals)):
            if pref[1] > intervals[i][0]:
                rez = rez + 1
            else:
                pref = intervals[i]

        return rez


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
s = Solution()
print(s.eraseOverlapIntervals(intervals))
