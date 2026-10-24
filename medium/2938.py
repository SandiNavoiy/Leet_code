class Solution:
    def minimumSteps(self, s: str) -> int:
        '''Отдельные черные и белые шарики'''
        rez = 0
        if "1" in s:
            ind = s.index("1")
            start = ind
            for c in range(ind, len(s)):
                if s[c] == "0":
                    rez += (c - start)
                    start +=1

            return rez
        else:
            return 0


s = Solution()
print(s.minimumSteps("101"))
