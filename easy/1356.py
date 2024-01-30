class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        """"""
        arr.sort(key=lambda x: (bin(x).count("1"), x))
        return arr


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
s = Solution()
print(s.sortByBits(arr))
# [0,1,2,4,8,3,5,6,7]
