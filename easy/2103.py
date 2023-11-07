class Solution:
    def countPoints(self, rings: str) -> int:
        """Кольца и стержни"""
        sunn = 0
        for i in range(len(rings) - 1):
            i = str(i)
            if "R" + i in rings and "B" + i in rings and "G" + i in rings:
                sunn = sunn + 1

        return sunn


rings = "B0B6G0R6R0R6G9"

s = Solution()
print(s.countPoints(rings))
