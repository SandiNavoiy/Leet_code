class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        """"""

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = bin(nums[i] | nums[j])

                if x[-1] == "0":
                    return True
        return False


nums = [1, 2]
s = Solution()
print(s.hasTrailingZeros(nums))
