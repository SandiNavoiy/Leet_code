from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        '''Показатель частоты встречаемости цифр'''

        d = dict(Counter(str(n)))
        rez = 0
        for i,j in d.items():
            rez += int(i) * int(j)



        return rez








n = 122
s = Solution()
print(s.digitFrequencyScore(n))
