class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        """Три суммы Фибоначчи"""
        ls = [0, 1, 1]
        s  = sum(ls)
        while s <= n:

            if s == n:
                return True
            ls.append(ls[-1] + ls[-2])
            s = ls[-1] + ls[-2] + ls[-3]

        return False


s = Solution()
print(s.threeFibonacciSum(16))
