class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """"""
        x = 0
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d and i not in arr2:
                    x = x + 1
        return x


arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6
s = Solution()
print(s.findTheDistanceValue(arr1, arr2, d))
