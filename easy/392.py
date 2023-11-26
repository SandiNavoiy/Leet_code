class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Является подпоследовательностью"""
        s_index = 0  # Индекс текущего символа в s

        for char in t:
            if s_index < len(s) and char == s[s_index]:
                # Если текущий символ в t совпадает с текущим символом в s,
                # увеличиваем индекс в s
                s_index += 1

        # Если все символы из s были найдены в t в правильном порядке,
        # то s является подпоследовательностью t
        return s_index == len(s)


s = "acb"
t = "ahbgdc"

sol = Solution()
print(sol.isSubsequence(s, t))