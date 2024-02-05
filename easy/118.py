class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """"""
        row = [1]
        for i in range(numRows):
            print(row)
            row = [sum(x) for x in zip([0] + row, row + [0])]
        return row


numRows = 5
s = Solution()
print(s.generate(numRows))
