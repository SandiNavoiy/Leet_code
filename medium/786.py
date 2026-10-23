class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        """K-я наименьшая простая дробь"""
        fractions = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append((arr[i] / arr[j], arr[i], arr[j]))

        fractions.sort(key = lambda x: x[0])


        return [fractions[k-1][1], fractions[k-1][2]]




s  =Solution()
print(s.kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))
