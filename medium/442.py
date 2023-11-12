class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """Найти все дубликаты в массиве"""
        ui = []
        for i in nums:
            if nums.count(i) == 2:
                ui.append(i)
        return list(set(ui))


nums = [4, 3, 2, 7, 8, 2, 3, 1]
sol = Solution()
print(sol.findDuplicates(nums))
