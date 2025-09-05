class Solution:
    def jump(self, nums: list[int]) -> int:
        """"""
        end = 0
        step = 0

        count = 0
        for i in range(len(nums) - 1):
            step = max(step, i + nums[i])
            if i == end:
                end = step
                count += 1
        return count


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
