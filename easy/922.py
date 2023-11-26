class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """Сортировка массива по четности II"""
        list_chet = []
        list_nechet = []
        for i in nums:
            if i % 2 == 0:
                list_chet.append(i)
            else:
                list_nechet.append(i)
        new = []
        for i in range(len(list_nechet)):
            new.append(list_chet[i])
            new.append(list_nechet[i])
        return new


nums = [4, 2, 5, 7]

s = Solution()
print(s.sortArrayByParityII(nums))
