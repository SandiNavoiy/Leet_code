class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        """"""
        x, y = 0, 0
        for i in commands:
            if i == "DOWN":
                y += 1
            elif i == "UP":
                y -= 1
            elif i == "RIGHT":
                x += 1
            elif i == "LEFT":
                x -= 1
        return y * n + x


n = 3
commands = ["DOWN", "RIGHT", "UP"]
s = Solution()
print(s.finalPositionOfSnake(n, commands))
