class Solution:
    def minTimeToType(self, word: str) -> int:
        time = len(word)
        cur = "a"
        for w in word:
            diff = abs(ord(w) - ord(cur))
            time += min(diff, 26 - diff)
            cur = w
        return time
