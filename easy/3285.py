class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        """"""
        rez = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                rez.append(i)

        return rez


s = Solution()
print(s.stableMountains([1, 2, 3, 4, 5], 2))  # [1,4]
