class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        '''Ограничение количества вхождений в отсортированном массиве'''

        rez = []
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            if d[num]<=k:
                rez.append(num)



        return rez




s = Solution()
print(s.limitOccurrences([1,1,1,2,2,3], 2))
