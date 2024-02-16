class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """"""
        while len(stones) > 2:
            stones.sort()
            print(stones)
            x = stones[-1]
            y = stones[-2]
            if x != y:
                stones.pop(-1)
                stones.pop(-1)
                stones.append(abs(y - x))
            else:
                stones.pop(-1)
                stones.pop(-1)
            print(stones)
            print("------")
        if len(stones) == 2:
            x = stones[-1]
            y = stones[-2]
            if x != y:
                stones.pop(-1)
                stones.pop(-1)
                stones.append(abs(y - x))
            elif x == y:
                return 0
        return stones[0]


stones = [2, 2]
s = Solution()
print(s.lastStoneWeight(stones))
