from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        '''Минимальное расстояние между тремя равными элементами I'''
        rez = len(nums) *1000
        flag = False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        flag = True

                        rez  = min(rez, abs(i - j) + abs(j-k) + abs(k-i))

        if flag:
            return rez
        else:
            return -1



s = Solution()
print(s.minimumDistance([1,2,1,1,3]))
