from typing import List


class Solution:
    @staticmethod
    def countSpecialNumbers(nums: List[int]) -> int:
        unique_nums = set(nums)
        count = 0

        for x in unique_nums:
            # Находим первый и последний индекс числа x
            first_idx = nums.index(x)
            last_idx = len(nums) - 1 - nums[::-1].index(x)  # хитрый способ найти последний индекс

            # Проверяем, что между first_idx и last_idx нет других чисел
            is_special = True
            for i in range(first_idx, last_idx + 1):
                if nums[i] != x:
                    is_special = False
                    break

            if is_special:
                count += 1

        return count


# Тесты из условия
sol = Solution()
print(sol.countSpecialNumbers([1, 2, 2, 1]))  # Вывод: 1
print(sol.countSpecialNumbers([3, 3, 1, 2, 2, 1]))  # Вывод: 2
