class Solution:
    def maximumTime(self, time: str) -> str:
        '''Новейшее время путем замены скрытых цифр'''

        if time[0] == "?":
            if time[1] in ("1","2","3","0", "?"):
                time = "2" + time[1:]
            else:
                time = "1" + time[1:]
        if time[1] == "?":
            if time[0] == "2":
                time = time[0] + "3" + time[2:]
            else:
                time = time[0] + "9" + time[2:]
        if time[3] == "?":
            time = time[0:3] + "5" + time[4:]
        if time[4] == "?":
            time = time[0:4] + "9"


        return time



s = Solution()
print(s.maximumTime("2?:?0"))
