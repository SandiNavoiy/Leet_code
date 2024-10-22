class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        """"""
        sum_player1 = 0
        sum_player2 = 0
        for i in range(len(player1)):
            if i < 1:
                sum_player1 = sum_player1 + player1[i]
                sum_player2 = sum_player2 + player2[i]
            elif i == 1:
                if player1[i - 1] == 10:
                    sum_player1 = sum_player1 + 2 * player1[i]
                else:
                    sum_player1 = sum_player1 + player1[i]

                if player2[i - 1] == 10:
                    sum_player2 = sum_player2 + 2 * player2[i]
                else:
                    sum_player2 = sum_player2 + player2[i]
            elif i >= 2:
                if player1[i - 1] == 10 or player1[i - 2] == 10:
                    sum_player1 = sum_player1 + 2 * player1[i]
                else:
                    sum_player1 = sum_player1 + player1[i]

                if player2[i - 1] == 10 or player2[i - 2] == 10:
                    sum_player2 = sum_player2 + 2 * player2[i]
                else:
                    sum_player2 = sum_player2 + player2[i]
            print(sum_player1)
            print(sum_player2)

        if sum_player1 > sum_player2:
            return 1
        elif sum_player1 < sum_player2:
            return 2
        elif sum_player1 == sum_player2:
            return 0


player1 = [5, 6, 1, 10]
player2 = [5, 1, 10, 5]
s = Solution()
print(s.isWinner(player1, player2))
