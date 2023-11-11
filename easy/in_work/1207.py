class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """Уникальное количество вхождений"""
        new = []
        for i in range(len(arr)):
            new.append(arr.count(arr[i]))

        return new


arr = [1, 2, 2, 1, 1, 3]
sol = Solution()
print(sol.uniqueOccurrences(arr))
