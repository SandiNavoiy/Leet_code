class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        """"""
        ans = []
        temp = 1
        while len(ans) < n:
            # находим цифры которые дают сумму к
            if k - temp not in ans:
                ans.append(temp)
            temp = temp + 1

        return sum(ans)


n = 5
k = 4
s = Solution()
print(s.minimumSum(n, k))
