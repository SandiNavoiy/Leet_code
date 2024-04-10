class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        ''''''
        key = keysPressed[0]
        time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):

            if  time < releaseTimes[i] - releaseTimes[i -1]:
                time = releaseTimes[i] - releaseTimes[i -1]
                key = keysPressed[i]
            elif time == releaseTimes[i] - releaseTimes[i -1]:
                if ord(key) < ord(keysPressed[i]):
                    key = keysPressed[i]


        return key
ReleaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
s = Solution()
print(s.slowestKey(ReleaseTimes, keysPressed))