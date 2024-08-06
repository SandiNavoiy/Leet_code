class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ''''''
        rez = len(nums)
        flag = 0

        for start in range((len(nums))):
            ss = 0
            for end in range(start, len(nums)):
                ss += nums[end]

                if ss >= target:
                    rez = min(rez, len(nums[start: end+1]))
                    flag = 1
                    break


        if flag == 1:
            return rez
        else:
            return 0

target = 11
nums = [1,2,3,4,5]
s = Solution()
print(s.minSubArrayLen(target, nums))