from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        """Вычисление десятичного представления"""
        rez = []
        s = str(n)
        for i in range(len(s)):
            if s[i] == '0':
                pass
            else:

                rez.append(int(s[i]) * 10 **(len(s) - i -1))

        return rez



s = Solution()
print(s.decimalRepresentation(537))
