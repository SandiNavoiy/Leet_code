class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        """"""
        new = []
        nums.sort()
        for i in queries:
            total = 0
            count = 0
            for j in nums:
                total = total + j
                count = count + 1
                if total > i:
                    count = count - 1
                    break
            new.append(count)

        return new


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
s = Solution()
print(s.answerQueries(nums, queries))
