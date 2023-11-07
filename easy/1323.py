class Solution:
    def maximum69Number(self, num: int) -> int:
        """Максимум 69 номеров"""

        ss = str(num)
        b = ss.replace("6", "9", 1)

        return int(b)


num = 9669
s = Solution()
print(s.maximum69Number(num))
