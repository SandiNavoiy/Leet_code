class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for r in range(n):
            m = max(nums[:r+1]) - min(nums[r:])

            if m <= k:
                return r

        return -1



s = Solution()
print(s.firstStableIndex([5,0,1,4], 3))
