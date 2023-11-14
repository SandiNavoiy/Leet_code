class Solution:
    def trimMean(self, arr: list[int]) -> float:
        """Среднее значение массива после удаления некоторых элементов """
        l = (5 * len(arr)) // 100
        arr_new = tuple(sorted(arr))


        new = []
        for i in range(l,len(arr_new) - l):
            print(arr_new[i])
            new.append(arr_new[i])

        return  sum(new) / len(new)


arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9 ,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]

s = Solution()
print(s.trimMean(arr))