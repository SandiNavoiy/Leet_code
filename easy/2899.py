class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        """"""
        seen = []
        ans = []
        k = 1
        for i in range(len(nums)):
            if nums[i] >= 0:
                seen = [nums[i]] + seen
                k = 1
            else:
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k - 1])
                    print(seen[k - 1])
                    k = k + 1

        return ans


nums = [1, -1, 2, -1, -1]
s = Solution()
print(s.lastVisitedIntegers(nums))
# [1, 2, 1]
