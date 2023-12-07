class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
       """"""
       x = arrivalTime + delayedTime
       if x < 24:
           return x
       elif x == 24:
           return 0
       else:
           return  x - 24
ArrivalTime = 1
DelayTime = 24
s = Solution()
print(s.findDelayedArrivalTime(ArrivalTime,DelayTime))
