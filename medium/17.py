import itertools
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """Буквенные комбинации номера телефона"""
        roman_numbers = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                         '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        if digits =="":
            return []

        new_list = []
        for i in digits:
            new_list.append(roman_numbers[i])
        combinations = list(itertools.product(*new_list))
        result_list = [''.join(combination) for combination in combinations]

        return result_list

digits = ""
s = Solution()
print(s.letterCombinations(digits))
