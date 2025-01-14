class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def check(balls):
            row = 1
            while True:
                color = (row + 1) % 2
                balls[color] -= row
                if balls[color] < 0:
                    return row - 1
                row += 1

        return max(
            check([red, blue]),
            check([blue, red]),
        )




red = 2
blue = 4
s = Solution()
print(s.maxHeightOfTriangle(red, blue))