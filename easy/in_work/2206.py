class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        """"""
        if len(nums) % 2 == 0:
            print(set(nums))
            if len(set(nums)) == len(nums) / 2:
                return True
        else:
            return False
nums = [3,2,3,2,2,2]
s = Solution()
print(s.divideArray(nums))