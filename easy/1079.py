from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        '''Варианты буквенных плиток'''
        tiles = list(tiles)

        s = set()
        for i in range(1, len(tiles)+1):
            x = list(permutations(tiles, i))


            for p in x:
                s.add(p)

        return len(s)




s = Solution()
print(s.numTilePossibilities('AAB'))