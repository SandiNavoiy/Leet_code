from statistics import median


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """"""
        ans = []
        med = median(nums)
        low = [i for i in nums if i < med]
        high = [i for i in nums if i >= med]
        while low or high:
            if low:
                ans.append(low.pop())
            if high:
                ans.append(high.pop())

        return ans


nums = [1, 2, 3, 4, 5]
s = Solution()
print(s.rearrangeArray(nums))
