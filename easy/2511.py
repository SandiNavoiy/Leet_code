class Solution:
    def captureForts(self, forts: list[int]) -> int:
        """"""
        step = []
        start = 0
        fin = 0
        forts_rev = forts[::-1]
        flag = False

        for i in range(len(forts)):
            if forts[i] == 1:
                start = i
                flag = True
            if forts[i] == -1 and flag == True:
                fin = i

                step.append(forts[start:fin].count(0))
                start = i
                flag = False
        start = 0
        fin = 0
        flag = False

        for i in range(len(forts_rev)):
            if forts_rev[i] == 1:
                start = i
                flag = True
            if forts_rev[i] == -1 and flag == True:
                fin = i

                step.append(forts_rev[start:fin].count(0))
                start = i
                flag = False
        if step != []:
            return max(step)
        return 0


forts = [0, -1, -1, 0, -1]
s = Solution()
print(s.captureForts(forts))
