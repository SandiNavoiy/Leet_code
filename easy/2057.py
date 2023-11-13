class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        """Наименьший индекс с равным значением"""
        summ = -1
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                summ = i
                break

        return summ


nums = [7, 8, 3, 5, 2, 6, 3, 1, 1, 4, 5, 4, 8, 7, 2, 0, 9, 9, 0, 5, 7, 1, 6]
s = Solution()
print(s.smallestEqual(nums))
