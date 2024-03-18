class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        ''' '''
        def encrypt(x):
            x = str(x)

            return int(max(x) * len(x))
        for i in nums:
            xx = sum([encrypt(x) for x in nums])
        return xx




nums = [10,21,31]
s = Solution()
print(s.sumOfEncryptedInt(nums))