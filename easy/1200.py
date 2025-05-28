class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """Минимальная абсолютная разность"""
        # сортируем массив для хохождения абсолютной разности
        arr.sort()
        # устанавливаем изначально максимальную обсолютную разнолсть,
        min_razn = 99999999999999999999999999
        # находим перебором эту разность до последнего элемента
        for i in range(1, len(arr)):
            min_razn = min(min_razn, abs(arr[i] - arr[i - 1]))
        # массив вывода
        res = []
        # находим пары, учитывая что в любом случае нас интересует разность только двух рядом стоящих элементов
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_razn:
                res.append([arr[i - 1], arr[i]])

        return res


s = Solution()
print(
    s.minimumAbsDifference(
        [
            188,
            9,
            -189,
            -112,
            165,
            4,
            -141,
            179,
            -154,
            258,
            53,
            71,
            201,
            204,
            121,
            215,
            259,
            -22,
            34,
            -213,
            -88,
            -192,
            118,
            -221,
            130,
            -86,
            209,
        ]
    )
)
