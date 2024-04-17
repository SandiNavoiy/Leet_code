from collections import Counter


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        """"""

        nums = nums[nums.index(key) + 1 : :]
        new = dict(Counter(nums))
        max_key = 0
        max_value = 0

        print(new)
        for i, j in new.items():
            if j > max_value:
                max_key = i
                max_value = j

        return max_key


nums = [2, 1, 2, 1, 2, 3]
key = 2
s = Solution()
print(s.mostFrequent(nums, key))
