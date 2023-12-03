class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new = []
        x = len(arr)
        for i in range(len(arr)):
            new.append(arr[i])
            if arr[i] == 0:
                new.insert(i, 0)
        arr = new[0: x + 1]
        return arr
arr = [1,0,2,3,0,4,5,0]
s = Solution()
print(s.duplicateZeros(arr))