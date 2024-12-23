class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ''''''

        count = 0
        if len(nums) == len(set(nums)):
            return count
        while True:
            if len(nums) <= 3:
                count += 1
                return count
            else:
                nums = nums[3:]
                count += 1
                if len(nums) == len(set(nums)):
                    return count

s = Solution()
print(s.minimumOperations([6,7,8,9]))
