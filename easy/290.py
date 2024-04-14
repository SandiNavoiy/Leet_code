class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """"""
        new = s.split()
        if len(new) != len(pattern):
            return False
        f = {}
        for i in range(len(pattern)):
            if pattern[i] not in f and new[i] not in f.values():
                f[pattern[i]] = new[i]
            elif pattern[i] not in f and new[i] in f.values():
                return False

            else:
                if new[i] != f[pattern[i]]:
                    return False

        return True


pattern = "abba"
s = "dog dog dog dog"
sol = Solution()
print(sol.wordPattern(pattern, s))
