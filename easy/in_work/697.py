class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """Степень массива"""
        sol = 0
        el = 0
        for i in nums:
            if nums.count(i) >= sol and i > el :
                sol = nums.count(i)
                el = i
        x = []
        left = nums.index(el)

        return sol, el


nums = [1,2,2,3,1]
s = Solution()
print(s.findShortestSubArray(nums))