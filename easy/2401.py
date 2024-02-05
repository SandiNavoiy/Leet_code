class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        """"""
        negat = []
        pozit = []

        for i in nums:
            if i < 0:
                negat.append(abs(i))
            else:
                pozit.append(i)
        x = set(negat) & set(pozit)
        if len(x) == 0:
            return -1
        else:
            return max(x)


nums = [-10, 8, 6, 7, -2, -3]
s = Solution()
print(s.findMaxK(nums))
