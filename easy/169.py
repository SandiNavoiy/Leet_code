class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """"""
        n = 0
        m = 0

        for i in nums:
            if nums.count(i) > n:
                n = nums.count(i)
                m = i
        return m


nums = [3, 2, 3]
s = Solution()
print(s.majorityElement(nums))
