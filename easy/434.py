class Solution:
    def countSegments(self, s: str) -> int:
        """Количество сегментов в строке"""
        new = []
        x = s.split(" ")
        for i in x:
            if i != "":
                new.append(i)
        return len(new)


s = "    "
sol = Solution()
print(sol.countSegments(s))
