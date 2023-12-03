class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """"""
        new = []
        new.append(list(set(nums1) - set(nums2)))
        new.append(list(set(nums2) - set(nums1)))
        return new
nums1 = [1,2,3]
nums2 = [2,4,6]
s = Solution()
print(s.findDifference(nums1, nums2))
