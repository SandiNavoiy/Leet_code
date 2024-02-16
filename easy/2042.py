class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        """"""
        ss = 0
        new = s.split(" ")
        for i in new:
            if i.isdigit():
                if int(i) > ss:
                    ss = int(i)
                else:
                    return False

        return True


s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
sol = Solution()
print(sol.areNumbersAscending(s))
