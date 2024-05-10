
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ''''''
        i = 0
        j = 0

        while i < len(typed):
            if typed[i] == name[j]:
                i += 1
                j += 1
            else:
                i += 1


        return len(name) == j
name = "alex"
typed = "aaleex"
s = Solution()
print(s.isLongPressedName(name, typed))