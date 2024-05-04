class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """"""
        stack = []
        step = 0
        for i in pushed:
            stack.append(i)
            while len(stack) != 0 and stack[-1] == popped[step]:
                stack.pop()
                step = step + 1
        return stack == []


push = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
s = Solution()
print(s.validateStackSequences(push, popped))
