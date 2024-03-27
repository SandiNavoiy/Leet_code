class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ''''''
        rez = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    x = i
                    y = j
        for i in board[x][y::]:
            if i == "p":
                rez = rez + 1
                break
            elif i == "B":
                break
        for i in board[x][y::-1]:
            if i == "p":
                rez = rez + 1
                break
            elif i == "B":
                break
        for i in board[x::]:


            if i[y] == "p":
                rez = rez + 1
                break
            elif i[y] == "B":
                break
        for i in board[x::-1]:


            if i[y] == "p":
                rez = rez + 1
                break
            elif i[y] == "B":
                break

        return rez


board = [[".", ".", ".", ".", ".", ".", "p", "."], ["p", ".", ".", ".", ".", ".", "R", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "p", "."]]

s = Solution()
print(s.numRookCaptures(board))
