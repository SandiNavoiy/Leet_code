from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        '''Сумма НОД образованных пар'''
        rez = 0
        prefixGcd = []
        maxx = nums[0]
        for num in nums:
            if num > maxx:
                maxx = num
            prefixGcd.append(gcd(num, maxx))
        prefixGcd.sort(reverse=True)
        left = 0
        right = len(prefixGcd) - 1
        while left < right:
            rez += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return rez



s = Solution()
print(s.gcdSum([2,6,4]))
