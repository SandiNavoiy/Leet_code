class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))


solution = Solution()
print(solution.maxDistinct("aabbcc"))
