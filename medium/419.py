class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        """"""
        count = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    flag = 1
                    if (i > 0 and board[i-1] [j] == "X") or (j > 0 and board[i][j-1]== "X"):
                        flag = 0
                    count = count + flag

        return count


board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
s = Solution()
print(s.countBattleships(board))
