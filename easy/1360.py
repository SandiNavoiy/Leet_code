from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """"""
        first_date = datetime.strptime(date1, "%Y-%m-%d").date()
        second_date = datetime.strptime(date2, "%Y-%m-%d").date()
        s = second_date - first_date
        return abs(s.days)


date1 = "2019-06-29"
date2 = "2019-06-30"
s = Solution()
print(s.daysBetweenDates(date1, date2))
