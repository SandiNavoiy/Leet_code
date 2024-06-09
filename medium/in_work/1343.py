class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        ''''''

        left = 0
        right = k
        n = len(arr)
        rez  = 0
        summ = sum(arr[left:right])
        while right<= n:
            print(arr[left:right])
            if summ /k >= threshold:
                rez = rez + 1

            summ = summ - arr[left]
            left = left + 1
            if right == n-1:
                break
            right = right + 1

            summ = summ + arr[right]
        return rez


arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
s = Solution()
print(s.numOfSubarrays(arr, k, threshold))