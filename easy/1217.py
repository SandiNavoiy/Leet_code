class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        ''''''

        chet = sum([1 for x in position if x % 2 == 0])
        nechet = sum([1 for x in position if x % 2 != 0])
        if chet > nechet:
            return nechet
        else:
            return chet
position = [1,2,3]
s = Solution()
print(s.minCostToMoveChips(position))