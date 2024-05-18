class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        """"""
        new_1 = []
        new_2 = []
        for i in intervals:
            if (
                i[0] <= newInterval[0] <= i[1]
                or i[0] <= newInterval[1] <= i[1]
                or (i[0] <= newInterval[0] and i[1] >= newInterval[1])
                or (i[0] >= newInterval[0] and i[1] <= newInterval[1])
            ):
                new_1.append(i)
            else:
                new_2.append(i)
        x = [new_1[0][0], new_1[-1][-1]]

        new_2.extend([x])
        new_2.sort()

        return new_2


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
s = Solution()
print(s.insert(intervals, newInterval))
