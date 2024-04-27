class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        """"""
        t = 0
        time_current = int(current[0:2]) * 60 + int(current[3:5])
        time_correct = int(correct[0:2]) * 60 + int(correct[3:5])
        x = abs(time_current - time_correct)

        t = x // 60

        x = x - 60 * (x // 60)



        if x ==0:
            return t


        t = t + x // 15

        x = x - 15 * (x // 15)

        if x ==0:
            return t
        t = t + x // 5
        x = x - 5 * (x // 5)
        if x ==0:
            return t

        return t + x


current = "02:30"
correct = "04:35"
s = Solution()
print(s.convertTime(current, correct))
