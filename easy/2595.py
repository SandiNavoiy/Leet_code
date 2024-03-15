class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        ''''''

        s = bin(n)[2:]
        s = s[::-1]
        print(s)
        even =0
        odd = 0
        for i in range(len(s)):
            if s[i] == "1":
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]
n = 17
s = Solution()
print(s.evenOddBit(n))