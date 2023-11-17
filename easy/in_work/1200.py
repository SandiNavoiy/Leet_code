class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """Минимальная абсолютная разница"""
        n = 0

        for i in arr:
            for j in arr:
                if abs(i - j) < n:
                    n = abs(i - j)
        return n


arr = [4,2,1,3]
s = Solution()
print(s.minimumAbsDifference(arr))

