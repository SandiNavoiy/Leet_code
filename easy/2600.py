class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        """"""

        new1 = (
            [1 for i in range(numOnes)]
            + [0 for j in range(numZeros)]
            + [-1 for x in range(numNegOnes)]
        )
        print(new1)
        if sum(new1[: k + 1]) > k:
            print("1")
            return k
        elif sum(new1[: k + 1]) < k:
            print("2")
            return sum(new1[:k])
        else:
            return k


numOnes = 6
numZeros = 6
numNegOnes = 6
k = 13
s = Solution()
print(s.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
