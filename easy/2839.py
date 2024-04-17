class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """"""
        if s1 == s2:
            return True
        if s1[0] != s2[0]:
            s1_new = s1[2] + s1[1] + s1[0] + s1[3]
        else:
            s1_new = s1
        if s1_new == s2:
            return True
        if s1[1] != s2[1]:
            s1_new = s1_new[0] + s1_new[3] + s1_new[2] + s1_new[1]
        if s1_new == s2:
            return True

        s2_new = s2[2] + s2[1] + s2[0] + s2[3]
        if s2_new == s1:
            return True
        s2_new = s2_new[0] + s2_new[3] + s2_new[2] + s2_new[1]
        if s2_new == s1:
            return True

        return False


s1 = "bnxw"
s2 = "bwxn"
s = Solution()
print(s.canBeEqual(s1, s2))
