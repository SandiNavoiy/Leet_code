
class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        ''''''
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]
nums1 = [2,6,4]
nums2 = [9,7,5]
s = Solution()
print(s.addedInteger(nums1, nums2))