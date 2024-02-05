class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        y = set(nums1) & set(nums2)

        z = set(nums1) & set(nums3)
        w = set(nums2) & set(nums3)
        a = list(y | z | w)
        return a


nums1 = [3, 1]
nums2 = [2, 3]
nums3 = [1, 2]
s = Solution()
print(s.twoOutOfThree(nums1, nums2, nums3))
