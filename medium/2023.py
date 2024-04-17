class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        ''''''
        sss = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    sss += 1
        return sss
nums = ["777","7","77","77"]
target = "7777"
s = Solution()
print(s.numOfPairs(nums, target))
