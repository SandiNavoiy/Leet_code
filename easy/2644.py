class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        """"""
        rez = 0
        rez_d = 0
        for i in divisors:
            temp = 0
            for j in nums:
                if j % i == 0:
                    temp = temp + 1
            if temp > rez:
                rez = temp
                rez_d = i
            elif temp == rez:
                rez_d = min(rez_d, i)

        if rez == 0:
            return min(divisors)

        return rez_d


nums = [31, 91, 47, 6, 37, 62, 72, 42, 85]
divisors = [95, 10, 8, 43, 21, 63, 26, 45, 23, 69, 16, 99, 92, 5, 97, 69, 33, 44, 8]
s = Solution()
print(s.maxDivScore(nums, divisors))
