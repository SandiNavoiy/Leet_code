from itertools import permutations


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        """Уникальные 3-значные четные числа"""

        return len([i for i in set(list(permutations(digits, 3))) if i[2]%2==0 and i[0] != 0])


s = Solution()
print(s.totalNumbers([1,2,3,4]))
