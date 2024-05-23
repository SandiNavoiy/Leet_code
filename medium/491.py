class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        subsequences = set()

        for num in nums:
            new_subsequences = set()
            new_subsequences.add((num,))
            for s in subsequences:
                if num >= s[-1]:
                    new_subsequences.add(s + (num,))
            subsequences |= new_subsequences
        return [s for s in subsequences if len(s) > 1]


nums = [4, 6, 7, 7]
s = Solution()
print(s.findSubsequences(nums))
