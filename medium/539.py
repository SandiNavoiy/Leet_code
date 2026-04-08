from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        '''Минимальная разница во времени'''
        # Конвертируем время в минуты

        lst  = [int(i[:2]) * 60 + int(i[3:]) for i in timePoints]
        # Сортируем список
        lst.sort()
        # Найдем минимальную разницу
        raznost = min([lst[i+1] - lst[i] for i in range(len(lst)-1)])

        # Найдем минимальную разницу между последним и первым временем

        return min(raznost, (1440 - lst[-1] + lst[0]))
s = Solution()
print(s.findMinDifference(["00:00","12:34","23:59","03:21","16:45","07:30","20:15","22:22"]))