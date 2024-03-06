class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        """"""
        # if len(nums) == 1:
        #     return nums[0]
        x = 0
        y = []
        for i in nums:
            if nums.count(i) > x and i % 2 == 0:
                x = nums.count(i)
                y.clear()
                y.append(i)
            elif nums.count(i) == x and i % 2 == 0:

                y.append(i)
        if x == 0:
            return -1
        else:
            return min(y)


nums = [1]
s = Solution()
print(s.mostFrequentEven(nums))

