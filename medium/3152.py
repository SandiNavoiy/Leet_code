class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        # Precompute the parity of the elements
        parity = [num % 2 for num in nums]

        results = []
        for query in queries:
            l, r = query
            is_special = True
            for i in range(l, r):
                if parity[i] == parity[i + 1]:
                    is_special = False
                    break
            results.append(is_special)

        return results


nums = [4, 3, 1, 6]
queries = [[0, 2], [2, 3]]
s = Solution()
print(s.isArraySpecial(nums, queries))
