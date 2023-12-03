class Solution:
    def reformatDate(self, date: str) -> str:
        m = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        new = ""
        x = ""
        y = ""
        if int(date[0:2]) <= 9:
            x = "0" + date[0:2]
        else:
            x = date[0:2]
        if m.index(date[5:8]) + 1 >= 10:
            y = str(m.index(date[5:8]) + 1)
        else:
            y= "0" + str(m.index(date[5:8]) + 1)

        new = date[9:13] + "-" + y + "-" + x
        return new

date = "20th Jan 2052"
s = Solution()
print(s.reformatDate(date))
#"2052-10-20"


