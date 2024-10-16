class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        """"""
        ans = []
        cur = 0

        for i in word:
            cur = (cur * 10 + int(i)) % m

            if cur == 0:
                ans.append(1)
            else:
                ans.append(0)

        return ans


word = "998244353"
m = 3
s = Solution()
print(s.divisibilityArray(word, m))
