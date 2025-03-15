from collections import Counter
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        cache = Counter(deck)

        if len(cache) == 1:
            return cache[deck[0]] > 1

        x = cache[deck[0]]

        for num in cache.values():
            x = gcd(x, num)

        return x > 1

s = Solution()
print(s.hasGroupsSizeX([1,2,3,4,4,3,2,1]))  # True
