class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicates = set()

        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        return list(duplicates)

nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDuplicates(nums))
