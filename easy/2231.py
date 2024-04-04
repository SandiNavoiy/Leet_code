class Solution:
    def largestInteger(self, num: int) -> int:
        """"""
        chet = []
        nechet = []
        rez = []

        for i in str(num):
            if int(i) % 2 == 0:
                chet.append(i)
            else:
                nechet.append(i)
        chet.sort()
        nechet.sort()
        for i in str(num):
            if int(i) % 2 == 0:
                rez.append(chet.pop())
            else:
                rez.append(nechet.pop())

        return int("".join(rez))


num = 1234
s = Solution()
print(s.largestInteger(num))
