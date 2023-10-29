class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        sum = 0
        for i in hours:
            if i >= target:
                sum += 1

        return sum


hours = [0, 1, 2, 3, 4]
target = 2

s = Solution()
print(s.numberOfEmployeesWhoMetTarget(hours, target))
