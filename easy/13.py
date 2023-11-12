class Solution:
    def romanToInt(self, s: str) -> int:
        """Роман в целое число"""
        s = (
            s.replace("CM", "DCCCC")
            .replace("CD", "CCCC")
            .replace("XC", "LXXXX")
            .replace("XL", "XXXX")
            .replace("IX", "VIIII")
            .replace("IV", "IIII")
        )

        roman_numbers = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        sum = 0
        for i in s:
            sum = sum + roman_numbers[i]

        return sum


s = "MCMXCIV"
# 1994
sol = Solution()
print(sol.romanToInt(s))
