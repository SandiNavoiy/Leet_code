class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """"""
        negat = []
        gat = []
        for i in arr1:
            if i not in arr2:
                negat.append(i)
        negat.sort()
        for y in arr2:
            if y in arr1:
                print(arr1.count(y))
                gat.append(y)

        return gat
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
s = Solution()
print(s.relativeSortArray(arr1, arr2))
#[2,2, 2,1,4,3,3,9,6,7,19]