class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """"""
        new = []
        x = 0
        y = 0
        for i in nums1:
            if i in nums2:
                x = x + 1
        for i in nums2:
            if i in nums1:
                y = y + 1
        new.append(x)
        new.append(y)
        return new


nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
s = Solution()
print(s.findIntersectionValues(nums1, nums2))
