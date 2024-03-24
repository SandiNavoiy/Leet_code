class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        """"""
        bbb = 0
        piles.sort(reverse=True)
        piles = piles[: int(2 * len(piles) / 3)]

        for i in range(1, len(piles), 2):
            bbb += piles[i]

        return bbb


piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
s = Solution()
print(s.maxCoins(piles))
