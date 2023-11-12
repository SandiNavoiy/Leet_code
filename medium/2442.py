class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        """ "Подсчитайте количество различных целых чисел после обратных операций Середина"""

        new = []
        for i in nums:
            j = str(i)

            new.append(int(j[::-1]))

        return len(set(nums + new))


nums = [1, 13, 10, 12, 31]


s = Solution()
print(s.countDistinctIntegers(nums))
