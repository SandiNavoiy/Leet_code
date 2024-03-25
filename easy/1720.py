class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        ''''''
        new = [first]
        for i in range(len(encoded)):
            new.append(encoded[i] ^ new[i])


        return new
encoded = [1,2,3]
first = 1
s = Solution()
print(s.decode(encoded, first))