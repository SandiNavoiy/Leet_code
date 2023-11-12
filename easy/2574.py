class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """Разница в суммах слева и справа"""
        summ_r = 0
        summ_l = 0
        summ_list = []
        for i in range(len(nums)):
            summ_r = sum(nums[i + 1 : len(nums)])
            summ_l = sum(nums[0:i])
            summ_list.append(abs(summ_l - summ_r))
        return summ_list


nums = [10, 4, 8, 3]
# [15,1,11,22]

s = Solution()
print(s.leftRightDifference(nums))
