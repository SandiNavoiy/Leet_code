class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        if n < 2:
            return nums
        ans = [[num] for num in nums]

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(ans[i]) < len(ans[j]) + 1:
                    ans[i] = ans[j] + [nums[i]]
        print(ans)
        return max(ans, key=lambda x: len(x))


nums = [1, 2, 3]
s = Solution()
print(s.largestDivisibleSubset(nums))
