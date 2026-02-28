class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        bit_length = 0  # длина текущего числа в битах

        for i in range(1, n + 1):
            # Если i является степенью 2, длина увеличивается на 1
            if i & (i - 1) == 0:
                bit_length += 1

            # Сдвигаем результат влево на длину текущего числа и добавляем само число
            result = ((result << bit_length) | i) % MOD

        return result


s = Solution()
print(s.concatenatedBinary(12))
