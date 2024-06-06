from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """"""
        x = dict(Counter(nums))
        rez = sorted(x.items(), key=lambda x: x[1], reverse=True)

        return [k for k, v in rez[:k]]


nums = [1, 1, 1, 2, 2, 3, 4, 4]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
