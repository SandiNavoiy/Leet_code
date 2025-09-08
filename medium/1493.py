class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """Самый длинный подмассив единиц после удаления одного элемента"""
        # начальные значения скользящего окна
        rez = 0
        start = 0
        zeros = 0
        # двигаем правую границу
        for end in range(len(nums)):
            # если нарвались на 0
            if nums[end] == 0:
                # увееличиваем счетсик на 1
                zeros = zeros + 1
                #
                while zeros > 1:
                    if nums[start] == 0:
                        # если 0 более чем 1 убираем 0 если попали на него
                        zeros = zeros - 1
                        # двигаем левую границу
                    start = start + 1
            # нахождем максимальное значение
            rez = max(rez, end - start)

        return rez


nums = [1, 1, 1, 0]


s = Solution()
print(s.longestSubarray(nums))
