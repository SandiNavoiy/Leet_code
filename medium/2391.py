class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        """"""
        m = 0
        p = 0
        g = 0
        time_m = 0
        time_p = 0
        time_g = 0
        # Наоодим последние индексы мусора
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                m = i
            if "P" in garbage[i]:
                p = i
            if "G" in garbage[i]:
                g = i
        # Считаем время обслуживания каждого мусора
        for i in range(m + 1):
            time_m += garbage[i].count("M")
        time_m = time_m + sum(
            travel[:m]
        )  # добавляем растоянние сбора до максимального располоджения мусора
        for i in range(p + 1):
            time_p += garbage[i].count("P")
        time_p = time_p + sum(travel[:p])

        for i in range(g + 1):
            time_g += garbage[i].count("G")
        time_g = time_g + sum(travel[:g])

        return time_p + time_g + time_m


garbage = ["MMM", "PGM", "GP"]
travel = [3, 10]

s = Solution()
print(s.garbageCollection(garbage, travel))
