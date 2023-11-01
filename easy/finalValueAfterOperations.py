class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        """Окончательное значение переменной"""
        x  = 0
        for i in operations:
            if i == '--X' or i == 'X--':
                x = x - 1
            else:
                x = x + 1
        return x

operations = ["--X","X++","X++"]
s = Solution()
print(s.finalValueAfterOperations(operations))