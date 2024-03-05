from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """"""
        if Counter(s) == Counter(t):
            return True
        return False


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
