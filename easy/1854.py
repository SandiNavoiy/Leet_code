class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        """ """
        d = {x: 0 for x in range(1950, 2051)}
        for i in range(1950, 2051):
            for j in logs:
                if j[0] <= i < j[1]:
                    d[i] = d[i] + 1
        sorted_tuple = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for i in sorted_tuple.keys():
            y = i
            break

        return y


logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
s = Solution()
print(s.maximumPopulation(logs))
