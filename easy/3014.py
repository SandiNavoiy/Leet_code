class Solution:
    def minimumPushes(self, word: str) -> int:
        """"""
        print(len(word))
        a = {}
        for i in range(0, len(word)):
            if i <= 7:
                if i not in a:
                    a[word[i]] = 1
            elif 7 < i <= 15:
                if i not in a:
                    a[word[i]] = 2
            elif 15 < i <= 23:
                if i not in a:
                    a[word[i]] = 3
            elif 23 < i:
                if i not in a:
                    a[word[i]] = 4

        print(a)
        return sum(a.values())


word = "bvlqfomhxkpactrjunsidzey"
s = Solution()
print(s.minimumPushes(word))
