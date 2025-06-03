class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        """Кратчайший подмассив с OR не менее KI"""

        # вводим максимальное число
        rez = 9999999999999999999999999999999
        # проводим итерацию по плаваюшему окну
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                #
                temp = temp | nums[j]
                # если побитовые операции, результат стал больше K, записываем в ответ минимальную длитнну и делаем брейк
                if temp >= k:
                    rez = min(rez, j - i + 1)
                    break
        #
        return rez if rez != 9999999999999999999999999999999 else -1


s = Solution()
print(s.minimumSubarrayLength(nums=[1, 2, 3], k=2))
