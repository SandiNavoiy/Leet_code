class Solution:
    def average(self, salary: list[int]) -> float:
        """Средняя зарплата без учета минимальной и максимальной зарплаты"""

        salary.sort()

        x = sum(salary[1:-1]) / len(salary[1:-1])
        return x


salary = [4000, 3000, 1000, 2000]

s = Solution()
print(s.average(salary))
