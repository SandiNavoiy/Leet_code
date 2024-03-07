class Solution:
    def isGood(self, nums: list[int]) -> bool:
        """"""
        num1 = sorted(nums)
        num2 = [x for x in range(1, max(nums) + 1)]
        num2.append(num1[-1])

        if num1 == num2:
            return True
        return False


nums = [2, 1, 3]
s = Solution()
print(s.isGood(nums))
