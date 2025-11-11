class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """"""
        i = 0
        j = 0
        flaf = 0
        while i < len(board) and j < len(board[0]):
            if board[i][j] == word[0]:





board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
s = Solution()
print(s.exist(board, word))
