class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction, row = "positive", -1
        rows = [""] * numRows

        for char in s:
            if direction == "positive":
                row += 1
            else:
                row -= 1

            rows[row] += char

            if row < 1:
                direction = "positive"
            if row == numRows - 1:
                direction = "negative"

        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
sol = Solution()
print(sol.convert(s, numRows))
