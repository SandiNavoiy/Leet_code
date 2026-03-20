from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        """Максимальный балл при разделении"""
        pref_sum = [nums[0]]
        rez = -9999999999999999999999999999999999999999999
#строим префиксную сумму
        for i in range(1,len(nums)):
            pref_sum.append(pref_sum[i-1] + nums[i])
#стоим минимальную величину в суффиксе. коряво но сторим
        nums_rev = nums[::-1]
        suffixMin = [nums_rev[0]]
        for i in range(1, len(nums)):
            suffixMin.append(min(suffixMin[i-1], nums_rev[i]))
#тестим условиееееееее
        suffixMin = suffixMin[::-1]
        for i in range(len(nums)-1):
            rez = max(rez, pref_sum[i] - suffixMin[i+1])
        print(pref_sum)
        print(suffixMin)
        return rez


s = Solution()
print(s.maximumScore([-7,-5,3]))