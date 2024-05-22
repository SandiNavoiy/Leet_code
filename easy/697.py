class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """Степень массива"""
        rez = len(nums)

        new = {}
        for i, j in enumerate(nums):
            if j not in new:
                new[j] = [i]
            else:
                new[j].append(i)

        maxx = max([len(x) for x in new.values()])
        for i in new.values():
            if len(i) == maxx:
                rez = min(rez, i[-1] - i[0])

        return rez + 1


nums = [1, 2, 2, 3, 1]
s = Solution()
print(s.findShortestSubArray(nums))
