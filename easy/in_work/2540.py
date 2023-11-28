class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        """"""
        x = set(nums1)&set(nums2)
        return min(x)


nums1 = [1,2,3]
nums2 = [2,4]
s = Solution()
print(s.getCommon(nums1, nums2))