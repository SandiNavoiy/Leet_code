class Solution:
    def hammingWeight(self, n: int) -> int:
        """"""
        n = str(n)
        return n.count("1")


n = "00000000000000000000000000001011"
s = Solution()
print(s.hammingWeight(n))
