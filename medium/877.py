class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        """"""
        # АПлиса всегда играет оптимально. поэтому ответ всегда один
        return True


piles = [3, 7, 2, 3]
s = Solution()
print(s.stoneGame(piles))
