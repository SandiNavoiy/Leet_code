class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """Уникальное количество вхождений"""
        new = []
        temp = []
        for i in range(len(arr)):
            if arr[i] not in temp:
                temp.append(arr[i])
                new.append(arr.count(arr[i]))

        return len(new) == len(set(new))


arr = [1, 2, 2, 1, 1, 3]
sol = Solution()
print(sol.uniqueOccurrences(arr))
