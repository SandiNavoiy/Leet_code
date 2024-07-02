class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """Bitwise complement"""
        rez = ""
        x = bin(n)[2:]
        for i in x:
            if i == "0":
                rez += "1"
            else:
                rez += "0"

        return int(rez, 2)


n = 5
s = Solution()
print(s.bitwiseComplement(n))
