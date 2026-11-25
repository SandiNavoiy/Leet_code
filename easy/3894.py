class Solution:
    def trafficSignal(self, timer: int) -> str:
        """ Цвет светофора"""
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        else:
            return "Invalid"





s = Solution()
print(s.trafficSignal(60))
print(s.trafficSignal(5))