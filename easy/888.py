class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        half = (alice + bob) // 2
        for i in aliceSizes:
            if half - (alice - i) in bobSizes:
                return [i, half - (alice - i)]
