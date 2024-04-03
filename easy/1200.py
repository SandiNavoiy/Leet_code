class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """Минимальная абсолютная разница"""
        arr.sort()
        razn = []
        rez = []
        for i in range(1, len(arr)):
            razn.append(abs(arr[i] - arr[i - 1]))
        print(razn)
        c = min(razn)
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) == c:
                rez.append([arr[i - 1], arr[i]])

        return rez


arr = [3, 8, -10, 23, 19, -4, -14, 27]
s = Solution()
print(s.minimumAbsDifference(arr))
# [[-14,-10],[19,23],[23,27]]
