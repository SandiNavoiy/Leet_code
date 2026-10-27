class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        '''Самая длинная последовательная последовательность'''
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1
        #удаляем дубликаты
        nums = list(set(nums))
        #сортируем
        nums.sort()
        #начало очередного этапа
        metka = 0
        #хранилище результатат
        rez= 0
        #индекс
        i = 0
        #длина посдедовательности (сразу минимальное 1)
        temp = 1
        while i < len(nums)-1:
            if nums[i+1] - nums[i] ==1:
                i = i+1
                temp = temp +1
            else:
                rez = max(rez,temp)
                #длина посдедовательности (сразу минимальное 1)
                temp = 1
                #перестааляем метртку врннд на символ
                metka = i + 1
                #и ниндеес. зачем считать то что уже посчитали
                i = metka
        #итого, если последовательность идет до конца
        rez = max(rez, temp)
        return rez


s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #9
print(s.longestConsecutive([100,4,200,1,3,2])) #4
print(s.longestConsecutive([1,0,1,2])) #3