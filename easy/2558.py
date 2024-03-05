class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        """"""
        gifts.sort()
        for i in range(k):
            gifts[-1] = int(gifts[-1] ** 0.5)
            gifts.sort()
        return sum(gifts)


gifts = [25, 64, 9, 4, 100]
k = 4
s = Solution()
print(s.pickGifts(gifts, k))
