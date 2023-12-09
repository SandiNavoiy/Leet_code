import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")


day = 18
month = 7
year = 1999

s = Solution()
print(s.dayOfTheWeek(day, month, year))
