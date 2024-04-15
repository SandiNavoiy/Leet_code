class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """"""
        mass = []
        otvet = []
        for i in range(1, len(target) + 1):
            if i in target:
                mass.append(i)
                otvet.append("Push")
                if mass == target:
                    return otvet
                    break
            else:
                otvet.append("Push")
                otvet.append("Pop")
        return otvet


target = [1, 3, 4, 6, 7, 8]
n = 9
s = Solution()
print(s.buildArray(target, n))
