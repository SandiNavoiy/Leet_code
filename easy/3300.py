class Solution:
    def minElement(self, nums: list[int]) -> int:
        """"""
        rez = []
        for i in nums:
            rez.append(sum([int(j) for j in str(i)]))

        return min(rez)


nums = [10, 12, 13, 14]
s = Solution()
print(s.minElement(nums))
