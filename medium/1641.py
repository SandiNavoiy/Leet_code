class Solution:
    def countVowelStrings(self, n: int) -> int:
        ''''''
        glass = ["a","e","i","o","u"]
        dp = [1,1,1,1,1]
        for i in range(1, n):
            for j in range(3,-1, -1):
                dp[j] =dp[j] +  dp[j+1]




        return sum(dp)


s = Solution()
print(s.countVowelStrings(33))