class Solution:
    def minOperations(self, logs: list[str]) -> int:
        ''''''
        x = 0
        for i in logs:
            if i == '../':
                if x <= 0:
                    x = 0
                else:
                    x = x -1
            elif i == './':
                pass
            else:
                x = x + 1
        return x


logs = ["d1/","../","../","../"]
s = Solution()
print(s.minOperations(logs))
#[5, -2, -4, 9, 5, 14]