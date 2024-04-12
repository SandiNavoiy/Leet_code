class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_index = {}  # создаем словарь для отслеживания индексов чисел
        for i, num in enumerate(nums):
            # Проверяем, есть ли число уже в словаре и его индекс ближе к i, чем k
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i  # Обновляем индекс числа
        return False
nums = [1,2,3,1,2,3]
k = 2
s = Solution()
print(s.containsNearbyDuplicate(nums, k))