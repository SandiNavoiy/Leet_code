class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """"""
        new = []
        for i in range(len(s)):
            temp_arr = []
            temp = s[i]
            temp_arr.append(i)
            for j in range(i, len(s)):
                if s[j] == temp:
                    temp_arr.append(j)
            new.append(temp_arr)
        new.sort(key=lambda x: x[-1] - x[0], reverse=True)

        if new[0][-1] - new[0][0] == 0:
            return -1
        elif new[0][-1] - new[0][0] == 1:
            return 0
        return new[0][-1] - new[0][0] - 1


s = "abca"
sol = Solution()
print(sol.maxLengthBetweenEqualCharacters(s))
