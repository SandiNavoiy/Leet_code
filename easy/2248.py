from collections import Counter
class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        if not nums:
            return []

        # Преобразуем первый список в множество
        result_set = set(nums[0])

        # Используем операцию пересечения множеств для остальных списков
        for lst in nums[1:]:
            result_set &= set(lst)

        # Возвращаем результат в отсортированном виде
        return sorted(result_set)


nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
s = Solution()
print(s.intersection(nums))
