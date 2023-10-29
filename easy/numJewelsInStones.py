class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """Количество вхождение камней"""
        sum = 0
        for i in jewels:
            x = stones.count(i)
            sum = sum + x

        return sum


sol = Solution()
number = sol.numJewelsInStones("z", "ZZ")
print(number)
