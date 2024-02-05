from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Пересечение двух массивов II"""
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        print(counter1)

        intersection = []
        for num, count in counter1.items():
            common_count = min(count, counter2.get(num, 0))
            intersection.extend([num] * common_count)

        return intersection


nums1 = [3, 1, 2]
nums2 = [1, 1]
s = Solution()
print(s.intersect(nums1, nums2))
