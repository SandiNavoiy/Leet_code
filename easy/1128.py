class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        domino_dict = {}
        pairs = 0

        for domino in dominoes:
            domino.sort()
            domino_key = tuple(domino)

            if domino_key in domino_dict:
                pairs += domino_dict[domino_key]
                domino_dict[domino_key] += 1
            else:
                domino_dict[domino_key] = 1

        return pairs


dominoes = [[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]
s = Solution()
print(s.numEquivDominoPairs(dominoes))
