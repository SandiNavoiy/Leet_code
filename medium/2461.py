class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        mx, total = 0, 0
        visit = set()
        while r < len(nums):
            while nums[r] in visit:
                total -= nums[l]
                visit.remove(nums[l])
                l += 1
            total += nums[r]
            visit.add(nums[r])
            if (r - l + 1) == k:
                mx = max(mx, total)
                total -= nums[l]
                visit.remove(nums[l])
                l += 1

            r += 1
        return mx


nums = [1, 2, 2]
k = 2
s = Solution()
print(s.maximumSubarraySum(nums, k))  # Output: 3
