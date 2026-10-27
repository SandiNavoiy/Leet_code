from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''Перестановка в строке'''
        #подсчитываем частоту в шаблоне
        s1_count = dict(Counter(s1))
        #и в начале строки
        s2_count = dict(Counter(s2[:len(s1)]))
        #если совпадабт то сразу ок
        if s1_count == s2_count:
            return True
        n = len(s1)
        #границы скользящего окна
        start = 0
        for end in range(n, len(s2)):
            if s2[end] in s2_count:
                s2_count[s2[end]] +=1
            else:
                s2_count[s2[end]] = 1
            #уменьшаем кол-во
            s2_count[s2[start]] -= 1
            #удаляем ели нет
            if s2_count[s2[start]] == 0:
                del s2_count[s2[start]]
            #двигаем окно
            start += 1
            #
            if s1_count == s2_count:
                return True

        return False

s = Solution()
print(s.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(s.checkInclusion(s1 = "ab", s2 = "eidboaoo"))