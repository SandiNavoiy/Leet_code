class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = []
        nums.sort()
        while len(nums) >= 2:
            x = 0
            y = 0

            x = nums.pop(0)
            y = nums.pop(0)
            new.append(y)
            new.append(x)

        return new


nums = [2, 7, 9, 6, 4, 6]
s = Solution()
print(s.numberGame(nums))
