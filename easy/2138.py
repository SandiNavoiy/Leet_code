class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        ''''''
        # Задаем новый массив
        new = []
        # Забиваем в это массив данные
        for i in range(0,len(s)+1,k):
            new.append(s[i: i+k])
        # Переменная разницы длинны последнего элемента от к
        razmer = k - len(new[-1])

        # Подпровляем последний элемент
        if len(new[-1]) == 0:
            new = new[0:-1]
        elif len(new[-1]) < k:
            new[-1] = new[-1] + fill * razmer

        return new

s = "abcdefghi"
k = 3
fill = "x"
sol = Solution()
print(sol.divideString(s, k, fill))