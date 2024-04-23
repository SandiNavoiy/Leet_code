class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """"""
        new = []
        nums.sort()
        print(nums)

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                new.append(nums[i : i + 3])
            else:
                return []
        return new


nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k = 2
s = Solution()
print(s.divideArray(nums, k))
