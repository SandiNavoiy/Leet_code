class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """"""
        n = len(pattern)
        ans = []
        stack = []
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == "I":
                while stack:
                    ans.append(stack.pop())

        return "".join(ans)


pattern = "IIIDIDDD"
s = Solution()
print(s.smallestNumber(pattern))
