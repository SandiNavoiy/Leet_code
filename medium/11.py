class Solution:
    def maxArea(self, height: list[int]) -> int:
        """Контейнер с большим количеством воды"""

        left = 0
        right = len(height) - 1
        sum = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
            sum = max(sum, min(height[left], height[right]) * (right - left))

        return sum



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


s = Solution()
print(s.maxArea)