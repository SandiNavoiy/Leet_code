class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        """"""
        ind = arr.index(max(arr))

        if ind == 0 or ind == len(arr) - 1:
            return False
        for i in range(1, ind):
            if arr[i] <= arr[i - 1]:
                return False
        for i in range(ind, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        return True


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = Solution()
print(s.validMountainArray(arr))
