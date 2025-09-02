class Solution:
    def countSubstrings(self, s: str) -> int:
        """Палиндромные подстроки"""
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
                else:
                    continue



        return count


s = Solution()
print(s.countSubstrings("aaa"))
