from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        frequency_map = Counter(nums)
        count = 0

        for i in frequency_map.values():
            if i == 1:
                return -1

            count += i // 3

            if i % 3 != 0:
                count += 1

        return count


nums = [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]
s = Solution()
print(s.minOperations(nums))
