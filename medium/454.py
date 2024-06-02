from collections import Counter


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        """"""
        t = dict(Counter(i + y for i in nums1 for y in nums2))
        print(t)

        rez = 0

        for i in nums3:
            for j in nums4:
                if -(i + j) in t:
                    rez = rez + t[-(i + j)]
        return rez


nums1 = [-1, -1]
nums2 = [-1, 1]
nums3 = [-1, 1]
nums4 = [1, -1]
s = Solution()
print(s.fourSumCount(nums1, nums2, nums3, nums4))
