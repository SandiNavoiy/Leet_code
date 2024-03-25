class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        ''''''
        rez = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    if x^y > rez:
                        rez = x^y
        return rez
nums = [1,2,3,4,5]
s = Solution()
print(s.maximumStrongPairXor(nums))