class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        # approach 1
        count,result=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                count=0
            result=result+count
        return result


nums = [1, 3, 0, 0, 2, 0, 0, 4]
s = Solution()
print(s.zeroFilledSubarray(nums))
