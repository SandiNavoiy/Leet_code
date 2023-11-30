class Solution:
    def secondHighest(self, s: str) -> int:
        temp = []
        for i in set(s):
            if ord(i) >= 97 and ord(i) <= 125:
                continue
            else:
                temp.append(int(i))
        if len(temp) < 2:
            return -1
        else:
            return sorted(temp)[-2]


s = "dfa12321afd"
sol = Solution()
print(sol.secondHighest(s))
