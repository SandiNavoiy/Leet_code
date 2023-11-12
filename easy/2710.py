class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        """Удалить конечные нули из строки"""
        s_new = ''.join(reversed(num))
        s_new1 = ''
        for i in range(len(s_new)):
          if s_new[i] == '0':
              s_new1 = s_new1
          else:
              s_new1 = s_new[i:]
              break

        return s_new1[::-1]


num = "51230100"
s = Solution()
print(s.removeTrailingZeros(num))