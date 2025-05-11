class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        """Сумма подмассивов переменной длины"""

        rez = []

        for i in range(len(nums)):
            rez.append(sum(nums[max(0, i - nums[i]) : i + 1]))

        return sum(rez)


s = Solution()
print(s.subarraySum([3, 1, 1, 2]))
