class Solution:
    def countSegments(self, s: str) -> int:
        """Количество сегментов в строке"""
        if s == "":
            return 0
        elif s.count(" ") == len(s):
            return 0
        else:
            n = s.count(" ")
            return n + 1


s = "                "
sol =  Solution()
print(sol.countSegments(s))
