class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        """Проверка различий между соседними цифрами."""

        flag = True

        for i in range(1,len(s)):
            if abs(int(s[i-1]) - int(s[i])) > 2:
                flag = False

        return flag


s = Solution()
print(s.isAdjacentDiffAtMostTwo("132"))
