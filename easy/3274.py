class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        """"""
        if (ord(coordinate1[0]) + ord(coordinate2[0])) % 2 == 0 and (
            int(coordinate1[1]) + int(coordinate2[1])
        ) % 2 == 0:
            return True
        elif (ord(coordinate1[0]) + ord(coordinate2[0])) % 2 != 0 and (
            int(coordinate1[1]) + int(coordinate2[1])
        ) % 2 != 0:
            return True
        return False


coordinate1 = "a1"
coordinate2 = "c3"
s = Solution()
print(s.checkTwoChessboards(coordinate1, coordinate2))
