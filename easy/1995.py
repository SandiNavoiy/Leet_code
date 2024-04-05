class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        ''''''
        ss = 0
        for a in range(len(nums )):
            for b in range(a, len(nums)):
                for c in range(b, len(nums)):
                    for d in range(b, len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d] and a < b < c < d:
                            ss = ss + 1

        return ss
nums = [1,2,3,6]
s = Solution()
print(s.countQuadruplets(nums))