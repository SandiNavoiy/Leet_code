class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

        new = [nums1[0],nums2[0]]
        for i in range(k-1):
            pass
        return new


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
s = Solution()
print(s.kSmallestPairs(nums1, nums2, k))