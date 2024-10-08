class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [0] * (n + 1)
        prime[0] = 1
        prime[1] = 1
        for x in range(2, n + 1):
            if prime[x] == 0:
                i = x
                while x * i <= n:
                    if prime[x * i] == 0:
                        prime[x * i] = 1
                    i += 1
        result = []
        for x in range(2, ((n // 2) + 1)):
            if prime[x] == 0 and prime[n - x] == 0:
                result.append([x, n - x])
        return result


n = 10
s = Solution()
print(s.findPrimePairs(n))
