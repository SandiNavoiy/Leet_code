class Solution:
    def kthCharacter(self, k: int) -> str:
        """"""
        word = "a"

        while len(word) < k:
            temp = ""
            for i in word:
                if i == "z":
                    temp += "a"
                else:
                    temp += chr(ord(i) + 1)
            word = word + temp

        return word[k - 1]


r = 5
s = Solution()
print(s.kthCharacter(r))
