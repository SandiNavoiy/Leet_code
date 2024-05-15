class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """"""
        high = len(nums) - 1
        low = 0
        if len(nums) == 1:
            if target in nums:
                return [0, 0]
            else:
                return [-1, -1]

        while low <= high:
            medium = (high + low) // 2

            if nums[medium] == target:
                print(medium)
                rez_end = medium
                rez_start = medium
                while nums[rez_start - 1] == target and rez_start > 0:
                    rez_start = rez_start - 1
                while rez_end < len(nums) - 1 and nums[rez_end + 1] == target:
                    rez_end = rez_end + 1
                return [rez_start, rez_end]

            elif nums[medium] > target:
                high = medium - 1

            elif nums[medium] < target:
                low = medium + 1

        return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
s = Solution()
print(s.searchRange(nums, target))
