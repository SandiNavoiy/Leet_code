class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """"""
        cdacha_5 = 0
        cdacha_10 = 0

        for i in bills:
            if i == 5:
                cdacha_5 += 1
            elif i == 10:
                if cdacha_5 == 0:
                    return False
                cdacha_5 -= 1
                if cdacha_5 < 0:
                    cdacha_5 = 0
                cdacha_10 += 1
            elif i == 20:
                if cdacha_5 == 0:
                    return False

                elif cdacha_5 == 0 and cdacha_10 == 0:
                    return False
                elif cdacha_5 == 1 and cdacha_10 == 0:
                    return False
                elif cdacha_5 == 2 and cdacha_10 == 0:
                    return False
                elif cdacha_5 == 0 and cdacha_10 == 1:
                    return False
                elif cdacha_10 == 0 and cdacha_5 >= 3:
                    cdacha_5 -= 3
                else:
                    cdacha_5 -= 1
                    if cdacha_5 < 0:
                        cdacha_5 = 0
                    cdacha_10 -= 1
                    if cdacha_10 < 0:
                        cdacha_10 = 0

        return True


bills = [5, 5, 5, 20, 5, 5, 5, 10, 20, 5, 10, 20, 5, 20, 5, 10, 5, 5, 5, 5]
s = Solution()
print(s.lemonadeChange(bills))
