class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        """"""
        x = 0
        for i in range(max(len(startTime), len(endTime))):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                x += 1
        return x


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
s = Solution()
print(s.busyStudent(startTime, endTime, queryTime))
