class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        ''''''

        t1_start = int(event1[0][0:2]) * 60 + int(event1[0][3:5])
        t2_start = int(event2[0][0:2]) * 60 + int(event2[0][3:5])
        t1_end = int(event1[1][0:2]) * 60 + int(event1[1][3:5])
        t2_end = int(event2[1][0:2]) * 60 + int(event2[1][3:5])
        if t1_start < t2_start:
            if t1_end >= t2_start:
                return True
        else:
            if t2_end >= t1_start:
                return True

        return False

s = Solution()
event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
print(s.haveConflict(event1, event2))
