from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """"""
        s1 = map(int, version1.split("."))
        s2 = map(int, version2.split("."))
        for i, j in zip_longest(s1, s2, fillvalue=0):
            if i > j:
                return 1
            elif i < j:
                return -1

        return 0


s = Solution()
version1 = "1.0"
version2 = "1.0.0.0"
print(s.compareVersion(version1, version2))
