from collections import Counter, defaultdict


class Solution:
    def occurrencesOfElement(
        self, nums: list[int], queries: list[int], x: int
    ) -> list[int]:
        """"""
        if x not in nums:
            return [-1] * len(queries)
        new = []
        dd = dict(Counter(nums))
        sss = []
        for i in range(len(nums)):
            if nums[i] == x:
                sss.append(i)
        for i in range(len(queries)):
            if dd[x] < queries[i]:
                new.append(-1)
            else:
                new.append(sss[queries[i] - 1])

        return new


nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1
s = Solution()
print(s.occurrencesOfElement(nums, queries, x))
