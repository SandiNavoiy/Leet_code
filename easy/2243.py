class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """"""
        if len(s) <= k:
            return s
        s = list(map(int, s))

        while len(s) > k:
            new = []
            for i in range(0, len(s), k):
                new.append(str(sum(s[i : i + k])))
            print(new)
            ttt = "".join(new)
            print(ttt)
            s = list(map(int, ttt))
        return ttt


s = "1"
k = 2
sol = Solution()
print(sol.digitSum(s, k))
