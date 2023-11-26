class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """Ранговое преобразование массива"""
        indexed_arr = {}
        sortes_arr = sorted(set(arr))
        for i in range(len(sortes_arr)):
            indexed_arr[sortes_arr[i]] = i + 1
        for i in range(len(arr)):
            arr[i] = indexed_arr[arr[i]]

        return arr


arr = [40, 10, 20, 30]
s = Solution()
print(s.arrayRankTransform(arr))
