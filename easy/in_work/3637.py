from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        '''Трионический массив I'''
        p = 0
        q = 0
        n = 0
        for i in range(len(nums)):
            if nums[i+1] < nums[i]:
                p = i
                break
        for i in range(p, len(nums)):
            if nums[i+1] > nums[i]:
                q = i
                break
        for i in range(q, len(nums)-1):
            if nums[i+1] < nums[i]:
                n = i
                break
            if i+1 == n-1:
                n = i

        return p, q, n




s = Solution()
print(s.isTrionic([1,3,5,4,2,6]))
