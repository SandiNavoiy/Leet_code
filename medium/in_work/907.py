class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        ''''''
        sss = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sss = sss + min(arr[i:j+1])

        return sss


arr = [11,81,94,43,3]
s = Solution()
print(s.sumSubarrayMins(arr))