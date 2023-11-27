class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        """Добавить в массив целых чисел"""
        x = "".join(map(str, num))
        new = int(x) + int(k)
        y = str(new)

        return y.split()


num = [1, 2, 0, 0]
k = 34
s = Solution()
print(s.addToArrayForm(num, k))
