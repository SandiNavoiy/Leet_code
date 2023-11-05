class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        """Усечь предложение"""
        new_str = ""
        listRes = list(s.split(" "))
        for i in range(k):
            new_str = new_str + str(listRes[i]) + " "

        return new_str[:-1]

s = "Hello how are you Contestant"
k = 4

sol = Solution()
print(sol.truncateSentence(s, k))
