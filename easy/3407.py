class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        """Шаблон сопоставления подстрок"""
        left_part, right_part = p.split("*")

        left_ind = s.find(left_part)
        right_ind = s.find(right_part, left_ind + len(left_part))


        return left_ind != -1 and right_ind != -1


s = "ojjju"
p = "*o"
sol = Solution()
print(sol.hasMatch(s, p))
