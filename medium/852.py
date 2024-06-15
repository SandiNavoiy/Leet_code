class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        """"""
        x = max(arr)
        return arr.index(x)


arr = [0, 2, 1, 0]
s = Solution()
print(s.peakIndexInMountainArray(arr))
