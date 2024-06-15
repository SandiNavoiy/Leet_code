class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        """"""
        new = []
        for i in range(len(variables)):
            if (
                ((variables[i][0] ** variables[i][1]) % 10) ** variables[i][2]
            ) % variables[i][3] == target:
                new.append(i)

        return new


variables = [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]]
target = 2
s = Solution()
print(s.getGoodIndices(variables, target))
