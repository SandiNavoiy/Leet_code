from bisect import insort, bisect_left
from statistics import median
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        ''''''
        # Список для хранения текущего окна
        window = sorted(nums[:k])
        # Результирующий список для медиан
        medians = [median(window)]



        for start in range(k,len(nums)):
            # Удаляем элемент, который выходит из окна
            window.pop(bisect_left(window, nums[start - k]))
            # Добавляем новый элемент
            insort(window, nums[start])
            # Добавляем текущую медиану в результат
            medians.append(median(window))
        return medians

nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
print(s.medianSlidingWindow(nums, k))