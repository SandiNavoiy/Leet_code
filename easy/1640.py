class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        ''''''

        new = []
        for i in arr:
            for j in pieces:
                if i == j[0]:
                    for k in j:
                     new.append(k)
        return new == arr
arr = [15,88]
Pieces = [[88],[15]]
s  = Solution()
print(s.canFormArray(arr, Pieces))