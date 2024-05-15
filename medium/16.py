class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """"""
        ans = 0
        raznica = 100000000000000000
        nums.sort()
        for i in range(len(nums) - 1):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                s = nums[i] + nums[end] + nums[start]
                if s == target:
                    return target
                elif abs(s - target) < raznica:
                    raznica = abs(s - target)
                    ans = s
                if s > target:
                    end = end - 1
                else:
                    start = start + 1

        return ans


nums = [-1, 2, 1, -4]
target = 1
s = Solution()
print(s.threeSumClosest(nums, target))
