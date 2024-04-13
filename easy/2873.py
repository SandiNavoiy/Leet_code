class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        ''''''
        sss = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k:

                        if (nums[i] - nums[j]) * nums[k] > sss:
                            sss = (nums[i] - nums[j]) * nums[k]

        if sss == 0:
            return 0
        return sss


nums = [12,6,1,2,7]
s = Solution()
print(s.maximumTripletValue(nums))