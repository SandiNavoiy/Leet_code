class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """"Максимальное произведение двух элементов в массиве"""
        new_arr = sorted(nums)
        sum = (new_arr[-1] -1) * (new_arr[-2] -1)
        return sum

nums = [3,4,5,2]
s = Solution()
print(s.maxProduct(nums))