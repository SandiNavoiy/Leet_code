class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        """"""
        averages = []
        n = len(nums)
        i = 0
        nums.sort()
        while i < int(n / 2):
            minn = nums.pop(0)
            maxx = nums.pop(-1)
            averages.append((minn + maxx) / 2)
            i = i + 1

        return min(averages)


nums = [7, 8, 3, 4, 15, 13, 4, 1]

s = Solution()
print(s.minimumAverage(nums))
