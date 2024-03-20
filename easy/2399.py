class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        ''''''
        nnn = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
               'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
               'x': 23, 'y': 24, 'z': 25}
        new = {}
        for index, char  in enumerate(s):
            if char not in new:
                new[char] = [index]
            elif char in new:
                new[char].append(index)
        for char, index in new.items():

            if index[1] - index[0] != distance[nnn[char]] + 1:
                return False

        return True



s = "abaccb"
distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sol = Solution()
print(sol.checkDistances(s, distance))
