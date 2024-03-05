from collections import Counter


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """"""
        arr = [[0, 0]]
        x = 0
        y = 0
        for i in range(len(path)):
            if path[i] == "N":
                y = y + 1
                if [x, y] not in arr:
                    arr.append([x, y])
                else:
                    return True
            elif path[i] == "S":
                y = y - 1
                if [x, y] not in arr:
                    arr.append([x, y])
                else:
                    return True
            elif path[i] == "W":
                x = x - 1
                if [x, y] not in arr:
                    arr.append([x, y])
                else:
                    return True
            elif path[i] == "E":
                x = x + 1
                if [x, y] not in arr:
                    arr.append([x, y])
                else:
                    return True

        return False


path = "NESWW"
s = Solution()
print(s.isPathCrossing(path))
