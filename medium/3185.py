from collections import defaultdict


class Solution:
    def countCompleteDayPairs(self, hours):
        d = defaultdict(int)
        rez = 0

        for i in hours:
            k = (24 - i % 24) % 24
            if k in d:
                rez = rez + d[k]

            d[i % 24] += 1
        return rez


hours = [72, 48, 24, 3]
s = Solution()
print(s.countCompleteDayPairs(hours))
