class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """"""
        #счетчик
        indxx = 0
        arr = [str(x) for x in range(low, high+1)]

        for i in arr:
            if len(i) % 2 == 0:
                left = i[:int(len(i)/2)]
                right = i[int(len(i) / 2):]
                sum_left = 0
                sum_right = 0
                for j in left:
                    sum_left = sum_left + int(j)
                for g in right:
                    sum_right = sum_right + int(g)
                if sum_left == sum_right:
                    indxx += 1
        return indxx



low = 1200
high = 1230
s = Solution()
print(s.countSymmetricIntegers(low, high))
