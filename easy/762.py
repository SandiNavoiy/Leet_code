class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """"""
        ss = (2, 3, 5, 7, 11, 13, 17, 19)
        count = 0
        for i in range(left, right + 1):

            if bin(i)[2:].count("1") in ss:
                count = count + 1

        return count


left = 6
right = 10
s = Solution()
print(s.countPrimeSetBits(left, right))
