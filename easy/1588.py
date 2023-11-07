class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        s = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                print(j)
                s += sum(arr[i : j + 1])
        return s


arr = [1, 4, 2, 5, 3]
s = Solution()
print(s.sumOddLengthSubarrays(arr))
