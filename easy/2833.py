class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        """"""
        step = 0

        if moves.count("L") >= moves.count("R"):
            new = [x if x != "_" else "L" for x in moves]
        else:
            new = [x if x != "_" else "R" for x in moves]
        for i in new:
            if i == "R":
                step += 1
            else:
                step -= 1
        return abs(step)


moving = "L_RL__R"
s = Solution()
print(s.furthestDistanceFromOrigin(moving))
