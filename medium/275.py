class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """"""

        t = len(citations)
        for i in citations:
            if i < t:
                t = t - 1
        return t


citations = [0, 1, 3, 5, 6]
s = Solution()
print(s.hIndex(citations))
