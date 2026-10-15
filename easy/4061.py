class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        """Минимальное количество ходов ферзя для достижения цели."""

        if (source[0] == target[0]) and (source[1] == target[1]):
            return 0
        elif (source[0] == target[0]) or (source[1] == target[1]):
            return 1
        elif abs(source[0] - target[0]) == abs(source[1] - target[1]):
            return 1
        else:
            return 2



s = Solution()
print(s.minQueenMoves([8,1], [1,8]))
