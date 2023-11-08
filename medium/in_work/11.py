class Solution:
    def maxArea(self, height: list[int]) -> int:
        """Контейнер с большим количеством воды"""
        sum = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if (min(height[i], height[j])) * (i - j) > sum:
                    sum = (min(height[i], height[j])) * (i - j)
        return sum

height = [1,8,6,2,5,4,8,3,7]


s = Solution()
print(s.maxArea(height))
#49