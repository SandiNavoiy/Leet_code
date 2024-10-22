class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        rez = []

        for i in range(len(s)):
            cnt = 0
            y, x = startPos

            for c in s[i:]:
                if c == "U":
                    y -= 1
                elif c == "D":
                    y += 1
                elif c == "R":
                    x += 1
                else:
                    x -= 1

                if x >= n or y >= n or x < 0 or y < 0:
                    break
                cnt += 1

            rez.append(cnt)

        return rez


n = 3
startPos = [0, 1]
s = "RRDDLU"
sol = Solution()
print(
    sol.executeInstructions(n, startPos, s)
)  # Ожидаемый результат: [1, 5, 4, 3, 1, 0]
