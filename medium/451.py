from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """"""
        cnt = dict(Counter(s))

        cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

        rs = []
        for x in cnt:
            rs.extend([x[0] * x[1]])
        return "".join(rs)


s = "tree"
sol = Solution()
print(sol.frequencySort(s))
