class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """Буквенные комбинации номера телефона"""
        roman_numbers = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                         '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        new_list = []
        for i in digits:
            new_list.append(roman_numbers[i])

        return new_list

digits = "29"
s = Solution()
print(s.letterCombinations(digits))
