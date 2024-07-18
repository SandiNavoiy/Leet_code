class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n = len(colors)
        if n < 3:
            return 0

        ans = 0
        for i in range(n - 2):
            if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
                ans += 1

        if colors[0] == colors[n - 2] and colors[0] != colors[n - 1]:
            ans += 1

        if colors[0] != colors[1] and colors[1] == colors[n - 1]:
            ans += 1

        return ans


colors = [0, 1, 0, 0, 1]
s = Solution()
print(s.numberOfAlternatingGroups(colors))
