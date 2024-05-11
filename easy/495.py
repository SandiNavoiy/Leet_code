class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        """"""
        t = duration
        for i in range(1, len(timeSeries)):
            if duration > timeSeries[i] - timeSeries[i - 1]:
                t = t + (timeSeries[i] - timeSeries[i - 1])
            else:
                t = t + duration

        return t


timeSeries = [1, 2, 3, 4, 5]
duration = 5
s = Solution()
print(s.findPoisonedDuration(timeSeries, duration))
