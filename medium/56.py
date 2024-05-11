class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """"""
        intervals.sort()
        new = []
        for i in intervals:
            if len(new) == 0 or new[-1][-1] < i[0]:
                new.append(i)
            else:
                new[-1][-1] = max(i[-1], new[-1][-1])
        return new


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
s = Solution()
print(s.merge(intervals))
