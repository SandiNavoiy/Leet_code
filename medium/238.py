class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """"""
        n = len(nums)
        new = [1] * n
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            # Формирование результирующего массива

        for i in range(n):
            new[i] = left[i] * right[i]

        return new


nums = [1, 2, 3, 4]
s = Solution()
print(s.productExceptSelf(nums))
