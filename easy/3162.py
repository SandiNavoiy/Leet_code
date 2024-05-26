class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """"""
        new = []
        for i in nums1:
            for j in nums2:
                if i % (j * k) == 0:
                    new.append([i, j])

        return len(new)


nums1 = [1, 2, 4, 12]
nums2 = [2, 4]
k = 3

s = Solution()
print(s.numberOfPairs(nums1, nums2, k))
