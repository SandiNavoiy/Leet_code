class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """Количество подмассивов с ограниченным максимумом"""

        rez = 0
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] > right:
                end = i
                start = i
                continue
            elif nums[i] >= left:
                end = i
            rez = rez + (end - start)


        return rez



s = Solution()
print(s.numSubarrayBoundedMax(nums = [2,1,4,3], left = 2, right = 3))
