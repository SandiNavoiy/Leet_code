class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ''''''
        high = len(nums)-1
        low = 0
        if len(nums)  == 1:
            if target in nums:
                return [0, 0]
            else:
                return [-1, -1]



        while low <= high:
            medium = (high + low) // 2

            if nums[medium] == target:
                if target == nums[medium-1]:
                    if medium-1 < 0:
                        return [medium, medium+1]

                    return [medium-1, medium]
                elif target == nums[medium+1]:
                    return [medium, medium+1]
                else:
                    return [medium, medium]
            elif nums[medium] > target:

                high = medium -1

            elif nums[medium] < target:

                low = medium +1

        return [-1, -1]
nums = [1,4]
target = 4
s = Solution()
print(s.searchRange(nums, target))
