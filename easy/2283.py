class Solution:
    def digitCount(self, num: str) -> bool:
        """. Проверьте, имеет ли число одинаковое количество цифр и значение цифры"""
        ee = []
        for i in range(len(num)):
            print(num.count(str(i)))
            print(num[i])
            print("----------")
            if num.count(str(i)) == int(num[i]):
                ee.append(True)
            else:
                ee.append(False)
                return False
        return ee


num = "030"
s = Solution()
print(s.digitCount(num))
