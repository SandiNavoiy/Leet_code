class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        """"""
        rez = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                arr = nums[:i] + nums[j:]
                if arr == sorted(arr) and len(arr) == len(set(arr)):
                    rez += 1
        return rez


nums = [1, 2, 3, 4]
s = Solution()
print(s.incremovableSubarrayCount(nums))
