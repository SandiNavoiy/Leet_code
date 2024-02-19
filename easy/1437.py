class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        a = []
        for i in range(len(nums)):
            if nums[i] == 1:
                a.append(i+1)
        return all((a[i+1]-a[i]) >= k+1 for i in range(len(a)-1))

nums = [1,1,1,1,1]
k = 0
s= Solution()
print(s.kLengthApart(nums, k))