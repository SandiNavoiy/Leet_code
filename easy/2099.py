class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        ''''''
        rez = []
        new = [x for x in nums]
        new.sort(reverse=True)
        new = new[:k]
        for i in range(len(nums)):
            if nums[i]  in new:
                rez.append(nums[i])
                new.pop(new.index(nums[i]))
        return rez
nums = [-1,-2,3,4]
k = 3
s = Solution()
print(s.maxSubsequence(nums, k))