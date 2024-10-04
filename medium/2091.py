class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        """"""
        minn = nums.index(min(nums))
        maxx = nums.index(max(nums))
        n = len(nums)

        return min(
            ((min(maxx, minn) + 1) + (n - max(maxx, minn))),
            ((n - min(maxx, minn))),
            ((1 + max(maxx, minn))),
        )


nums = [2, 10, 7, 5, 4, 1, 8, 6]
s = Solution()
print(s.minimumDeletions(nums))
