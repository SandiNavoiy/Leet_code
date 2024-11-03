class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        # Сортируем списки игроков и тренеров
        players.sort()
        trainers.sort()

        # Инициализируем два указателя и счётчик
        i, j = 0, 0
        count = 0

        # Пробегаемся по обоим спискам
        while i < len(players) and j < len(trainers):
            # Если текущий тренер подходит для текущего игрока
            if trainers[j] >= players[i]:
                count += 1  # Увеличиваем счётчик совпадений
                i += 1  # Переходим к следующему игроку
            # В любом случае переходим к следующему тренеру
            j += 1

        return count


players = [4, 7, 9]
trainers = [8, 2, 5, 8]
s = Solution()
print(s.matchPlayersAndTrainers(players, trainers))
