class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        """"""
        gg = 0
        new = str(num)
        for i in range(len(new) - k + 1):
            if int(new[i : i + k]) != 0 and num % int(new[i : i + k]) == 0:
                gg += 1

        return gg


num = 430043
k = 2
s = Solution()
print(s.divisorSubstrings(num, k))
