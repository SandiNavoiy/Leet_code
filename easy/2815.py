class Solution:
    def maxSum(self, nums: list[int]) -> int:
        ''''''

        nums.sort(reverse=True)
        max1 =nums[0]
        maxx = []
        for i in str(max1):
            maxx.append(i)
        for i in nums:
            for j in str(i):
                if j == maxx[0]:
                    second  = i
        if max1 <10:
            return -1

        return max1, second



nums = [31,25,72,79,74]
s= Solution()
print(s.maxSum(nums))