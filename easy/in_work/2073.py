class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        """"""
        count = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] = tickets[i] - 1
                    count = count + 1
                    if tickets[k] <= 0:  # Проверяем, не закончились ли билеты типа k
                        break

        return count


tickets = [84, 49, 5, 24, 70, 77, 87, 8]
k = 3
s = Solution()
print(s.timeRequiredToBuy(tickets, k))
