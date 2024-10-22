class Solution:
    def minSwaps(self, s: str) -> int:
        """"""
        c = 0

        stack = []
        for i in s:
            if i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    c = c + 1
                    stack.append(i)
                else:
                    stack.pop()

        return c


s = "]]][[["
sol = Solution()
print(sol.minSwaps(s))
