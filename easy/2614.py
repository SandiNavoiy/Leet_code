import math


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        new = []
        n = len(nums)  # Размерность квадратной матрицы

        def is_prime(n):
            """проверка на простоту"""
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        for i in range(n):
            if is_prime(nums[i][i]):
                new.append(nums[i][i])  # Элементы главной диагонали
            if is_prime(nums[i][n - 1 - i]):
                new.append(nums[i][n - 1 - i])  # Элементы побочной диагонали

        if len(new) != 0:
            return max(new)
        return 0


nums = [
    [788, 645, 309, 559],
    [624, 160, 435, 724],
    [770, 483, 95, 695],
    [510, 779, 984, 238],
]
s = Solution()
print(s.diagonalPrime(nums))
