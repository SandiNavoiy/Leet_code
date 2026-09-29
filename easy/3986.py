from datetime import datetime


class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        '''Количество секунд, прошедших между двумя моментами времени.'''
        startTime = datetime.strptime(startTime, "%H:%M:%S")
        endTime = datetime.strptime(endTime, "%H:%M:%S")
        rez = str(endTime - startTime).split(":")
        rez = int(rez[0])*3600 + int(rez[1])*60 + int(rez[2])



        return rez



s= Solution()
startTime = "01:00:00"
endTime = "01:00:25"
print(s.secondsBetweenTimes(startTime, endTime))
