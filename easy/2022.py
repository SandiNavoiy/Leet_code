class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        """"""
        new = []
        if m * n != len(original):
            return []
        for i in range(0, len(original) - n + 1, n):
            new.append(original[i : i + n])

        return new


original = [1, 2, 3, 4]
m = 2
n = 2
s = Solution()
print(s.construct2DArray(original, m, n))
