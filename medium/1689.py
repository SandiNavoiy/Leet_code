class Solution:
    def minPartitions(self, n: str) -> int:
        """
        :param n:
        :return:
        """
        for i in range(9, -1, -1):
            if str(i) in n:
                return i


n = "32"
s = Solution()
print(s.minPartitions(n))
