import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        """День года"""
        date_time_obj = datetime.datetime.strptime(date, "%d.%m.%Y").date()
        start_of_year = datetime.date(date_time_obj.year, 1, 1)

        # Вычисление разницы в днях
        days_difference = (date_time_obj - start_of_year).days + 1
        return days_difference


date = "09.01.2019"
s = Solution()
print(s.dayOfYear(date))
