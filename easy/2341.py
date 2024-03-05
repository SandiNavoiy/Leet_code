class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        """"""
        inn = 0
        inn_1 = 0
        x = {}
        for i in nums:
            x[i] = nums.count(i)
        for i in x.values():
            if i % 2 == 0:
                inn = inn + int(i / 2)
            else:
                inn = inn + int(i / 2)
                inn_1 = inn_1 + 1

        return [inn, inn_1]


nums = [1, 3, 2, 1, 3, 2, 2]
s = Solution()
print(s.numberOfPairs(nums))
