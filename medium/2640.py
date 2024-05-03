class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        """"""

        conver = [nums[0] + nums[0]]
        mm = nums[0]

        for i in range(1, len(nums)):
            mm = max(mm, nums[i])
            conver.append(conver[i - 1] + nums[i] + mm)

        return conver


nums = [2, 3, 7, 5, 10]
s = Solution()
print(s.findPrefixScore(nums))
