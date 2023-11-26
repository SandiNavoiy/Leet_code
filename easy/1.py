class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Две суммы"""
        new = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    new.append(i)
                    new.append(j)
        return list(set(new))


nums = [3, 2, 4]
target = 6
s = Solution()
print(s.twoSum(nums, target))
