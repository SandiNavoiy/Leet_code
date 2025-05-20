class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        """Построить минимальный побитовый массив"""
        #
        n = len(nums)
        #задаем пустой массив ответа
        ans = []
        #прогоняем в два цикла сначала исходгик, а потом числа меньшие чем то что в нем дано
        for i in range(n):
            for j in range( nums[i]):
                #проверяем условие задачи
                if j | (j + 1) == nums[i]:
                    #добавляем искомое число
                    ans.append(j)
                    break
            #если не нашли то добавляем в ответ -1
            else:
                ans.append(-1)
        return ans






s = Solution()
print(s.minBitwiseArray([2,3,5,7]))