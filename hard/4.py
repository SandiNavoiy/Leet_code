import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """"""
        x = np.array(nums1 + nums2)

        return np.median(x)


nums1 = [1, 3]
nums2 = [2]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
