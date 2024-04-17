class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """"""
        if set(s1) != set(s2):
            return False
        cc = 0
        for i in range(len(s1)):
            if s1.count(s1[i]) != s2.count(s2[i]):
                print(s1.count(s1[i]))
                print(s2.count(s2[i]))
                print(s1[i])
                return False
            if s1[i] != s2[i]:
                cc += 1
        print(cc)
        if cc == 0 or cc == 2:
            return True
        return False


s1 = "siyolsdcjthwsiplccjbuceoxmpjgrauocx"
s2 = "siyolsdcjthwsiplccpbuceoxmjjgrauocx"
s = Solution()
print(s.areAlmostEqual(s1, s2))
