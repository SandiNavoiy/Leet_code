from collections import Counter, defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        """Подсчет значений с равномерным интервалом между ними."""

        d = {}
        for key,value in dict(Counter(nums)).items():
            if value==3:
                d[key]=value

        lst_ind = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in d:
                lst_ind[nums[i]].append(i)


        rez = 0

        for key,value in lst_ind.items():
            if value[1] - value[0] == value[2] - value[1]:
                rez += 1



        return rez



s = Solution()
print(s.countSpecialIntegers([1,8,1,5,1,5,8,5]))
