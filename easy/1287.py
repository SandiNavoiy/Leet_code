class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        """"""
        x = len(arr)
        for i in arr:
            print(arr.count(i))
            if arr.count(i) / x >= 0.25:
                return i


arr = [1, 2, 3, 3]
s = Solution()
print(s.findSpecialInteger(arr))
