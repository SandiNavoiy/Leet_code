class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        """"""
        rez = []
        for i in nums:
            if nums.count(i) == 2 and i not in rez:
                rez.append(i)

        return rez


nums = [0, 3, 2, 1, 3, 2]
s = Solution()
print(s.getSneakyNumbers(nums))
