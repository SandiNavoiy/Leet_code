class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """Количество подмассивов с ограниченным максимумом"""
        rez = []
        start = 0
        end = 1
        temp = nums[start]
        while start <= len(nums) and end < len(nums)+1:
            if temp <= right:
                rez.append(nums[start:end])
                if end < len(nums):
                    temp = max(nums[end], temp)
                end = end + 1
            else:
                while start < end:
                    start += 1

                end = end +1
                temp = nums[start]

        return len(rez)



s = Solution()
print(s.numSubarrayBoundedMax(nums = [2,1,4,3], left = 2, right = 3))
