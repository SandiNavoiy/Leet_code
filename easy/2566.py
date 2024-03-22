class Solution:
    def minMaxDifference(self, num: int) -> int:
        ''''''
        minn = 0
        maxx = num

        x = str(num)
        for i in x:

            if int(i) < 9:
                maxx = int(x.replace(i, '9'))
                break
        for i in x:
            if int(i) > 0:
                minn = int(x.replace(i, '0'))
                break

        return maxx - minn
num = 99999
s = Solution()
print(s.minMaxDifference(num))
