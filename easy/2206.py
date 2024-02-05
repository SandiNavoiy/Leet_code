class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        """"""
        n = len(nums)
        if n % 2 == 0:
            for i in nums:
                if nums.count(i) % 2 != 0:
                    return False
        else:
            return False
        return True


nums = [3, 2, 3, 2, 2, 2]
s = Solution()
print(s.divideArray(nums))
