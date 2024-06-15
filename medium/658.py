class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        """"""
        left = 0
        right = len(arr) - 1
        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left = left + 1
            else:
                right = right - 1
        return arr[left : right + 1]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
s = Solution()
print(s.findClosestElements(arr, k, x))
