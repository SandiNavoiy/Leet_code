class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """"""
        for i in range(len(board)):
            for j in range(len(board[0])):
                pass


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
s = Solution()
print(s.exist(board, word))
