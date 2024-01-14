class Solution:
    def pivotInteger(self, n: int) -> int:
        """"""
        left_sum = 0
        new = [i for i in range(n + 1)]
        total_sum = sum(new)

        for i in new:
            total_sum -= i
            if left_sum == total_sum:
                return i

            left_sum += i
        return -1


n = 4
s = Solution()
print(s.pivotInteger(n))
