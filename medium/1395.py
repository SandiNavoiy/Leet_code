


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        """Подсчитайте количество команд"""
        rez= 0
        n = len(rating)

        #делаем перебор по элементам
        for i in range(1,n):
            left_min = 0
            left_max = 0
            right_min = 0
            right_max = 0
            #далее смотрим количество элеменртов больши меньших справа
            for j in range(i+1,n):
                if rating[i] > rating[j]:
                    right_min +=1
                elif rating[i] < rating[j]:
                    right_max +=1
            #далее смотрим количество элеменртов больши меньших слева
            for j in range(0,i):
                if rating[i] < rating[j]:
                    left_max +=1
                elif rating[i] > rating[j]:
                    left_min +=1

            #считаем перемножением большие * меньшие + меньшие * большие = число комбинаций
            rez = rez + (left_min *right_max ) + (left_max * right_min)

        return rez


s = Solution()
print(s.numTeams([2,5,3,4,1]))