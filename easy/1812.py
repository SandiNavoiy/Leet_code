class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        """"""
        new = list(coordinates)
        if new[0] == "a" or new[0] == "c" or new[0] == "e" or new[0] == "g":
            if int(new[1]) % 2 == 0:
                return True
            return False
        else:
            if int(new[1]) % 2 == 0:
                return False
            return True


coordinates = "a1"
s = Solution()
print(s.squareIsWhite(coordinates))
