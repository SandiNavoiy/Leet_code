class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        """"""
        ss = nums[0] + nums[1]
        eee = 0
        if len(nums) % 2 == 0:
            for i in range(0, len(nums) - 1, 2):
                if nums[i] + nums[i + 1] == ss:
                    eee += 1
                else:
                    break
        else:
            for i in range(0, len(nums) - 2, 2):
                if nums[i] + nums[i + 1] == ss:
                    eee += 1
                else:
                    break
        return eee


nums = [1, 1, 1, 1, 1, 1]
s = Solution()
print(s.maxOperations(nums))
