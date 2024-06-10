class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        ''''''
        n = len(arr)
        rez  = 0
        sss = sum(arr[:k])
        for i in range(n-k + 1):
            if sss / k >= threshold:
                rez += 1
            if i + k< n:
                sss = sss - arr[i] + arr[i+k]

        return rez

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
s = Solution()
print(s.numOfSubarrays(arr, k, threshold))