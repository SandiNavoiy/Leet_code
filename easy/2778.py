# class Solution:
#     def sumOfSquares(self, nums: list[int]) -> int:
#         """"""
#         l = len(nums)
#
#         new = []
#         for i in nums:
#             if l % i == 0:
#                 new.append(i * i)
#         return sum(new)
#
class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n=len(nums)

        ans=0
        for i in range(n):
            if n%(i+1)==0:
                print(nums[i])
                ans=ans+nums[i]**2

        return ans

nums = [2,7,1,19,18,3]
s = Solution()
print(s.sumOfSquares(nums))
