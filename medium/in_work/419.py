class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        """"""
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    print("ok")


board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
s = Solution()
print(s.countBattleships(board))
