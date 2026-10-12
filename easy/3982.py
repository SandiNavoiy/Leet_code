class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        """Сумма целых чисел с максимальным диапазоном цифр."""
        rez = []
        mmax = 0

        for i in nums:
            t = [int(i) for i in str(i)]
            raz = max(t) - min(t)
            if raz > mmax:
                mmax = raz
                rez.clear()
                rez.append(t)
            elif raz == mmax:
                rez.append(t)

        r = 0
        for i in rez:
            t = ""
            for j in i:
                t = t + str(j)
            r += int(t)
        return r


s= Solution()
print(s.maxDigitRange([5724,111,350]))
