class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """Плюс один"""
        new = int("".join(map(str, digits)))
        new = str(new + 1)
        n = []
        for i in new:
            n.append(int(i))

        return n


digits = [1, 2, 3]
s = Solution()
print(s.plusOne(digits))
