class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        sm = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sm += nums[i]
        lst = []
        for i in range(len(queries)):
            prev = nums[queries[i][1]]
            nums[queries[i][1]] += queries[i][0]
            curr = nums[queries[i][1]]
            if prev % 2 == 0:
                if curr % 2 == 0:
                    sm += curr - prev
                else:
                    sm -= prev
            else:
                if curr % 2 == 0:
                    sm += curr
            lst.append(sm)
        return lst


nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
s = Solution()
print(s.sumEvenAfterQueries(nums, queries))
# [8,6, 2,4]
