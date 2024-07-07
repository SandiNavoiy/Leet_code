class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        ''''''
        n = len(arr)
        rez = [0]*(n+1)
        for i in range(1, n+1):
            summ = 0
            for j in range(1, min(k,i)+1):
                summ = max(summ, arr[i-j])
                rez[i]=max(rez[i],rez[i-j]+summ*j)

        return rez[n]
arr = [1,15,7,9,2,5,10]
k = 3
s  = Solution()
print(s.maxSumAfterPartitioning(arr, k))