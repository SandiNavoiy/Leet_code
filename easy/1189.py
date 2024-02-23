from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """"""
        word = "balloon"
        new = Counter(text)
        return min(new["b"], new["a"], new["l"] // 2, new["o"] // 2, new["n"])


text = "nlaebolko"
s = Solution()
print(s.maxNumberOfBalloons(text))
