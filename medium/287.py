from collections import Counter

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        ''''''
        x = dict(Counter(nums))
        new = sorted(x.items(), key=lambda i:i[1],reverse=True)

        return new[0][0]

nums = [1,3,4,2,2,4,4,4]
s = Solution()
print(s.findDuplicate(nums))

from collections import Counter


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Создаем словарь с подсчетом каждого числа в списке
        count = Counter(nums)

        # Сортируем словарь по значениям в порядке убывания
        sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)

        # Возвращаем ключ с наибольшим значением
        return sorted_count[0][0]
