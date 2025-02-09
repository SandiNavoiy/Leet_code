class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''НЕОПТИМИЗИРОВАННОЕ РЕШЕНИЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        LLL = len(s)
        start = 0
        end = 0

        def searc( l, r):
            while l >= 0 and r < LLL:
                if s[l] == s[r]:
                    l -= 1
                    r += 1

                else:
                    break
            return l+1, r

        for i in range(len(s)):
            l1, r1 = searc(i, i)
            if r1- l1 > end -start:
                start = l1
                end = r1
            l2, r2 = searc(i, i+1)
            if r2 - l2 > end - start:
                start = l2
                end = r2

        return s[start:end]
s = "babad"

sol = Solution()
print(sol.longestPalindrome(s))