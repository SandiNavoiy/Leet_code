class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:
        """"""
        ind = 0
        start = 0
        dlina = 0


        for i in events:
            if i[1] - start > dlina:
                dlina = i[1] - start
                ind = i[0]
            elif i[1] - start == dlina:

                ind = min(i[0], ind)
            start = i[1]

        return ind
s = Solution()

print(s.buttonWithLongestTime([[9,4],[19,5],[2,8],[3,11],[2,15]]))