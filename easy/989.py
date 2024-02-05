class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        """Добавить в массив целых чисел"""
        x = "".join(map(str, num))
        try:
            new = int(x) + k
            y = str(new)
        except OverflowError:
            raise ValueError("Result exceeds the limit for integer string conversion.")

        ss = []
        for i in y:
            ss.append(int(i))

        return ss


num = [1, 2, 0, 0]
k = 34
s = Solution()
print(s.addToArrayForm(num, k))
