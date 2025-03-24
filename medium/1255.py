class Solution:
    def twoEggDrop(self, n: int) -> int:
        ''''''
        i= 1
        rez = []
        while n > 0:
            rez.append(n)
            n  = n -i
            i = i + 1

        return len(rez)
n = 100
s = Solution()
print(s.twoEggDrop(n))
