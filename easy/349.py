class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Пересечение двух массивов"""
        return list(set(nums1) & set(nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
s = Solution()
print(s.intersection(nums1, nums2))
