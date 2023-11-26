class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        amm = 100
        temp = (amm - purchaseAmount) // 10
        if (amm - purchaseAmount) % 10 <= 5:
            return temp * 10
        else:
            return (temp + 1) * 10


purchaseAmount = 15

s = Solution()
print(s.accountBalanceAfterPurchase(purchaseAmount))
