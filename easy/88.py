class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1[0: m]
        num2 = nums2[0: n]
        nums = num1 + num2
        nums.sort()
        nums1 = []
        nums1 = nums
        return nums1





nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
s = Solution()
print(s.merge(nums1, m, nums2, n))
