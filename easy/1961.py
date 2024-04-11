class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        """"""
        bb = ""
        for word in words:
            bb = bb + word
            if bb == s:
                return True
        return False


s = "iloveleetcode"
words = ["i", "love", "leetcode", "apples"]
sol = Solution()
print(sol.isPrefixString(s, words))
