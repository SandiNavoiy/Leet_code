class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''Разрыв слова'''
        wordDict.sort(key=len, reverse=True)

        for i in wordDict:
            while i in s:
                s = s.replace(i, "")

        if len(s) < 1:
            return True
        else:
            return False
s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))