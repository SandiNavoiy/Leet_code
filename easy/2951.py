class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        """"""
        new = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                new.append(i)
        return new


mountain = [1, 4, 3, 8, 5]
s = Solution()
print(s.findPeaks(mountain))
