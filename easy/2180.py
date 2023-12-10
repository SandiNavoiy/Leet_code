class Solution:
    def countEven(self, num: int) -> int:
        """"""
        x = 0
        for i in range(1,num + 1):
            temp = str(i)
            y = 0
            for j in temp:
                y = y + int(j)
            if y % 2 ==0:
                x = x +1
        return x



num = 11
s = Solution()
print(s.countEven(num))
