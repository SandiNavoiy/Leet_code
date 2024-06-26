class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        ''''''
        n = len(hours)
        rez = []
        for i in range(n):
            for j in range(i+1, n):
                if (hours[i]+hours[j]) % 24 == 0:
                    rez.append([i,j])

        return len(rez)
hours = [12,12,30,24,24]
s = Solution()
print(s.countCompleteDayPairs(hours))