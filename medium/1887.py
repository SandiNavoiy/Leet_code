class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        """"""
        rez = 0
        uniques = list(set(nums))
        n = len(uniques) - 1
        uniques.sort(reverse=True)
        d = {}
        for i, j in enumerate(uniques):
            d[j] = i
        for i in nums:
            rez = rez + (n) - d[i]

        return rez


nums = [1, 1, 2, 2, 3]

s = Solution()
print(s.reductionOperations(nums))
