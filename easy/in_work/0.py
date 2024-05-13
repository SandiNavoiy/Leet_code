class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """"""
        rez = 0
        char_dict  = {}
        index = 0
        for i, char in enumerate(s):
            if char in char_dict and char_dict[char] >= index:
                rez = max(rez, i - index)
                index = char_dict[char] + 1
            char_dict[char]  = i

        return max(rez, len(s) - index)

s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))