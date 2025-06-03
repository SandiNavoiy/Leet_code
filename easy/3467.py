class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        """Преобразование массива по четности"""
        chet = 0
        nechet = 0

        for i in nums:
            if i % 2 == 0:
                chet += 1

            else:
                nechet += 1
        return [0] * chet + [1] * nechet


s = Solution()
print(s.transformArray([4, 3, 2, 1]))
