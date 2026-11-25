class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        """Минимальная длина струны после сбалансированного удаления"""
        return abs(s.count("a") - s.count("b"))

s = Solution()
print(s.minLengthAfterRemovals("aabbab"))
