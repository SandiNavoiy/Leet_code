class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        ''''''
        nums.sort()
        n = 0
        for i in nums:
            if i < k:
                 n  = n +1
        return n

nums = [760340387,289254123,628299234,204198715,565672759,684967229,303459334,302262994,770720781,383343826,148523784,750183433,778902176,930418501,520286131,441750197,402643198,547480026,799770607,303114486,481644752,320289220,792197603,44751343,828179295,804048578,468569446,555743704,416141129,865011209,56010709,133835994,200083188,740956911,842527451,728469270,370323078,880010797,977376598,598070033,866374140,110775975,609860085]
k = 10

s = Solution()
print(s.minOperations(nums, k))