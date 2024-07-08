class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """"""
        hash_map = {}
        rez = []
        for i in range(len(s)):
            hash_map[s[i]] = i
        start, end = 0, 0
        for i in range(len(s)):
            end = max(i, hash_map[s[i]], end)
            if end == i:
                rez.append(end - start + 1)
                start = end + 1

        return rez


s = "ababcbacadefegdehijhklij"
sol = Solution()
print(sol.partitionLabels(s))
