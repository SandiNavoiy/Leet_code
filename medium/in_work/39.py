class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """Сумма комбинаций"""
        rez = []

        for i in range(len(candidates)):
            temp = target
            for j in range(i, len(candidates)):
                print(temp, candidates[j])
                while temp // candidates[j] > candidates[j]:
                    rez.append(candidates[j])
                    temp -= candidates[j]

        return rez


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
