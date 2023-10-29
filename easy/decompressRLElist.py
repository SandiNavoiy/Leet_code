class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        generated = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            generated += [val] * freq
        return generated


nums = [1,2,3,4]

s = Solution()
print(s.decompressRLElist(nums))

