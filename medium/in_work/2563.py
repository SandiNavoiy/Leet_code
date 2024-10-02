class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        """"""
        eee = []
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    ans = ans + 1
                    eee.append([i, j])
                else:
                    continue

        return ans


nums = [0, 0, 0, 0, 0, 0]
lower = 0
upper = 0
s = Solution()
print(s.countFairPairs(nums, lower, upper))
