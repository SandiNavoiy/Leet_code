class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """"""
        new = []
        for i in nums1:
            for j in range(nums2.index(i), len(nums2)):
                if i == nums2[-1]:
                    new.append(-1)
                    break
                elif i > max(nums2[j:]):
                    new.append(-1)
                    break
                elif i < nums2[j]:
                    new.append(nums2[j])
                    break
        return new


nums1 = [1, 3, 5, 2, 4]
nums2 = [5, 4, 3, 2, 1]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))
# [-1,3,-1]
