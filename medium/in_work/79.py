class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """"""
        i = 0
        j = 0
        while i < len(board) and j < len(board[0]):
            if board[i][j] == word[0]:
                break
            else:
                j += 1
                i += 1

        while i < len(board) and j < len(board[0]):
            if

        print(i, j)


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
s = Solution()
print(s.exist(board, word))
