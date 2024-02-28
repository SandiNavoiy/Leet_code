class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """"""
        for i in words:
            if i == i[::-1]:
                return i
        return ""


word = ["abc", "car", "ada", "racecar", "cool"]
s = Solution()
print(s.firstPalindrome(word))
