class Solution:
    def partitionString(self, s: str) -> int:
        """Returns the"""
        count = 0
        temp = set()
        for i in s:
            if i in temp:
                temp.clear()
                count = count + 1

            temp.add(i)
        return count + 1


s = "abacaba"
sol = Solution()
print(sol.partitionString(s))
