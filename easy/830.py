class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        l = r = 0
        ans = []
        while r < len(s):
            while r < len(s) and s[l] == s[r]:
                r += 1
            if r - l >= 3:
                ans.append([l, r - 1])
            l = r
        return ans



        return new
s = "abcdddeeeeaabbbcd"
sol = Solution()
print(sol.largeGroupPositions(s))