class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        """"""
        minn = min(len(s1), len(s2), len(s3))
        c = 0
        for i in range(minn):
            if s1[i] == s2[i] == s3[i]:
                c = c + 1
            else:
                break
        if c == 0:
            return -1
        minn = c
        return len(s1) - minn + len(s2) - minn + len(s3) - minn


s1 = "dac"
s2 = "bac"
s3 = "cac"
s = Solution()
print(s.findMinimumOperations(s1, s2, s3))
