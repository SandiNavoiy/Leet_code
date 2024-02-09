class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """"""
        new = []
        for i in nums1:
            for j in range(len(nums2) - 1):
                if i == nums2[j]:
                    if nums2[j] < nums2[j + 1]:
                        new.append(nums2[j + 1])
                    else:
                        new.append(-1)
            if i == nums2[-1]:
                new.append(-1)

        return new


nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))
#[7,7,7,7,7]