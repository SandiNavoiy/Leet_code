from collections import Counter
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ''''''

        ls = []
        for i in responses:
            for j in set(i):
                ls.append(j)

        d = dict(Counter(ls))
        d = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
        m = max(d.values())
        for k, v in d.items():
            if v == m:
                return k

s = Solution()
print(s.findCommonResponse([["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]))