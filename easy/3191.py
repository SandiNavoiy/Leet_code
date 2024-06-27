class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """"""
        c = 0

        n = len(nums)
        rez = [1 for i in range(n)]
        if nums == rez:
            return c
        for i in range(n - 2):
            if nums[i] == 0:
                c = c + 1
                nums[i] = 1

                nums[i + 1] = 1 - nums[i + 1]

                nums[i + 2] = 1 - nums[i + 2]

        if nums == rez:
            return c
        return -1


nums = [1, 1, 1]
s = Solution()
print(s.minOperations(nums))
