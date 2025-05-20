class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        """Наименьший индекс с суммой цифр, равной индексу"""

        for i in range(len(nums)):
            if sum([int(x) for x in str(nums[i])]) == i:
                return i


        return -1


s = Solution()
print(s.smallestIndex([1,3,2]))
