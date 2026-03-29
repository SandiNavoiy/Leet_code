class Solution:
    def removeZeros(self, n: int) -> int:
        """"""

        rez = ""
        for i in str(n):
            if i != "0":
                rez += i

        return int(rez)




s = Solution()
print(s.removeZeros(1020030))
