from collections import Counter


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        ''''''
        l = int(len(candyType)/2)
        x = dict(Counter(candyType))
        if l >= len(x):
            return len(x)
        else:
            return l



candyType = [1,1,2,2,3,3]
s = Solution()
print(s.distributeCandies(candyType))