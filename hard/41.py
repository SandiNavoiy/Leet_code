class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            d[i] = i
        i = 1
        while True:
            if i in d:
                pass
            else:
                return i
            i = i + 1

        return d


nums = [3, 4, -1, 1]
s = Solution()
print(s.firstMissingPositive(nums))
