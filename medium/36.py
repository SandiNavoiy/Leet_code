import collections


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ''''''
        mapp =  collections.defaultdict(list)
        for rov in range(9):
            for col in range(9):
                char = board[rov][col]
                if char != ".":
                    if char in mapp:
                        for i in mapp[char]:
                            if i[0] == rov or i[1] == col or (i[0]//3 == rov//3 and i[1]//3 == col//3):
                                return False
                    mapp[char].append((rov,col))

        return True




board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s = Solution()
print(s.isValidSudoku(board))
