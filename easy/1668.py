class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(sequence) < len(word):
            return 0
        k = 1
        ans = 0

        while k * word in sequence:
            ans += 1
            k += 1
        return ans


sequence = "aaaba aaaba aab a aaaba aaaba aaaba aaaba"
word = "aaaba"
s = Solution()
print(s.maxRepeating(sequence, word))
