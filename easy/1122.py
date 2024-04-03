class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """"""
        new = []
        new1 = [x for x in arr1 if x not in arr2]
        new1.sort()
        for i in arr2:
            while i in arr1:
                new.append(i)
                arr1.remove(i)
        return new + new1


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
s = Solution()
print(s.relativeSortArray(arr1, arr2))
# [2,2, 2,1,4,3,3,9,6,7,19]
