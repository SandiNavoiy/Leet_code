class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return rec1[2] > rec2[0] and rec1[3] > rec2[1] and rec2[2] > rec1[0] and rec2[3] > rec1[1]


rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]
s = Solution()
print(s.isRectangleOverlap(rec1, rec2))
