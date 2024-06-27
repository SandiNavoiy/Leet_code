class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the 32-bit integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Main division loop using bit shifts
        result = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        # Apply the sign
        result *= sign

        # Clamp the result to the 32-bit integer range
        return max(MIN_INT, min(MAX_INT, result))


dividend = 10
divisor = 3
s = Solution()
print(s.divide(dividend, divisor))
