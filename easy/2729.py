class Solution:
    def isFascinating(self, n: int) -> bool:
        """"""
        n1 = n * 2
        n2 = n * 3
        s = str(n1) + str(n2) + str(n)
        print(s)
        if (
            "1" in s
            and "2" in s
            and "3" in s
            and "4" in s
            and "5" in s
            and "6" in s
            and "7" in s
            and "8" in s
            and "9" in s
            and "0" not in s
            and len(s) == 9
        ):
            return True
        return False


n = 783
s = Solution()
print(s.isFascinating(n))
