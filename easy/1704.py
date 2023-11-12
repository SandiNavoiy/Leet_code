class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """Определите, похожи ли половинки струны"""
        w = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        l = len(s)

        left = []
        right = []
        for i in s[0 : int(l / 2)]:
            if i in w:
                left.append(i)
        for j in s[int(l / 2) :]:
            print(j)
            if j in w:
                right.append(j)

        return len(left) == len(right)


s = "AbCdEfGh"

sol = Solution()
print(sol.halvesAreAlike(s))
