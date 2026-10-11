class Solution:
    def minRotations(self, s: str) -> int:
        """Минимальное количество оборотов для набора номера I"""
        #суммарный ответ
        rez = 0
        #временная переменная
        temp = 0

        for i in s:
            #преобразуем
            i = int(i)
            #считаем как выгоднее идти по или против часовой
            rez += min(abs(i-temp), abs (10 - abs(i-temp)))
            temp = i


        return rez




sol = Solution()
print(sol.minRotations("0192837465"))

