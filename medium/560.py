class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ''''''
        rez = 0

        for i in range(len(nums)+1):

            for j in range(i+1,len(nums)+1):
                print(nums[i:j])
                if sum(nums[i:j]) == k:
                    rez += 1
                    break

        return rez
nums = [1]
k = 0
s = Solution()
print(s.subarraySum(nums, k))