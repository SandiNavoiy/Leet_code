from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """Возможность отправки посылок в течение D дней."""
        #находим имни и мак. мин это максимальный вес в массиве макс это сумма
        minn = max(weights)
        maxx = sum(weights)
        #среднее
        mid = (minn + maxx) // 2
        d = 1
        #цикл бинарного поиска
        while minn < maxx:
        #временная пеерменная для учета веса груза
            temp = 0
            #считаем вес груза
            for weight in weights:
                temp += weight
                #если перегруз то обнуляем и добавляем день, если  равно то обнулим на след шаг
                if temp > mid:
                    d += 1
                    temp = weight
#если дней погрузки больше то двигаем левую границу вправо
            if d > days:
                minn = mid + 1
   #  иначе двигаем правую границу влево до средней
            else:
                maxx = mid
    #начинвем заново, обновляем счетчики
            d = 1
            mid = (minn + maxx) // 2

        return minn






s = Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))