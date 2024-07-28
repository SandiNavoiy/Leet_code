class Solution:
    def findLengthOfShortestSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        # Найти максимальную левую отсортированную часть
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:  # Массив уже отсортирован
            return 0

        # Найти максимальную правую отсортированную часть
        right = n - 1
        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1

        # Минимальное удаление при использовании только левой или правой части
        result = min(n - left - 1, right)

        # Проверка возможных соединений левой и правой частей
        i, j = 0, right
        while i <= left and j < n:
            if nums[i] <= nums[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result


nums = [1, 2, 3]
s = Solution()
print(s.findLengthOfShortestSubarray(nums))
