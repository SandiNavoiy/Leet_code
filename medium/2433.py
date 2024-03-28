class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        x = []

        for i in range(0, len(pref)):
            if i == 0:
                x.append(pref[i])
            else:
                x.append(pref[i] ^ pref[i - 1])
        return x


pref = [5, 2, 0, 3, 1]
s = Solution()
print(s.findArray(pref))
# [5,7,2,3,2]
