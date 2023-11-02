class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        """Максимальное значение строки в массиве"""
        m = []
        for i in strs:
            if i.isdigit():
                m.append(int(i))
            else:
                m.append(len(i))

        return max(m)


strs = ["alic3", "bob", "3", "4", "00000"]
s = Solution()
print(s.maximumValue(strs))
