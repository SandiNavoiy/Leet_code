class Solution:
    def findGCD(self, nums: list[int]) -> int:
        """Найдите наибольший общий делитель массива"""
        new = sorted(nums)

        for i in range(new[0]+1, 0, -1):
            if new[-1] % i == 0 and new[0] % i == 0:
                return i


nums = [7,5,6,8,3]
s = Solution()
print(s.findGCD(nums))
