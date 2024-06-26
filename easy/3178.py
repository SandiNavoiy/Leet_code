class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        ''''''
        col = k // (n- 1)
        ost = k % (n- 1)
        if col % 2 == 0:
            return ost
        else:
            return (n- 1) -  ost





n = 5
k = 6
s = Solution()
print(s.numberOfChild(n, k))