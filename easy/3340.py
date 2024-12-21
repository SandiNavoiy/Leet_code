class Solution:
    def isBalanced(self, num: str) -> bool:
        """"""
        chet = 0
        nechet = 0
        rez = list(map(int, num))
        for i in range(len(rez)):
            if i % 2 == 0:
                chet += rez[i]
            else:
                nechet += rez[i]



        return  chet == nechet

n = "1234"
s = Solution()
print(s.isBalanced(n))
