class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """"""
        citations.sort()
        t = len(citations)
        for i in citations:
            if i < t:
                t = t - 1
        return t


citations = [11, 15]
s = Solution()
print(s.hIndex(citations))
