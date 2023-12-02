class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """Максимум последовательных"""
        x = []
        y = 0

        for i in nums:
            if i == 1:

                y += 1

            elif i == 0 :
                x.append(y)
                y = 0
        x.append(y)


        return max(x)

nums = [1,1,0,1,1,1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))
