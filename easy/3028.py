class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        """"""
        step = 0
        result = 0
        for i in nums:
            step += i
            if step == 0:
                result += 1

        return result


nums = [2, 3, -5]
s = Solution()
print(s.returnToBoundaryCount(nums))
