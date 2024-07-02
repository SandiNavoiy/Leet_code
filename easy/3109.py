class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ''''''
        rez = 0
        for i in nums:
            if i % 3 != 0:
                rez += 1
        return rez
nums = [1,2,3,4]
s = Solution()
print(s.minimumOperations(nums))