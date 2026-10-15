class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        '''Максимальная пара произведений с целевой суммой'''
        d = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and (nums[i] > nums[j]) and (i!=j):
                    d[nums[i] * nums[j]] = [i,j]



        if d:
            return d[max(d.keys())]
        else:
            return [-1, -1]




s = Solution()
print(s.maxProductPair(nums = [4,5,-6,-7], target = -2))


