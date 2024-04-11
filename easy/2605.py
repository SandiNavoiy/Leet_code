class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        """"""
        new = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    new.append(int(str(i)))
                else:
                    new.append(int(str(i) + str(j)))
                    new.append(int(str(j) + str(i)))

        return min(new)


nums1 = [7, 5, 6]
nums2 = [1, 4]
s = Solution()
print(s.minNumber(nums1, nums2))
