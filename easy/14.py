class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ''''''
        if len(strs) == 1:
            if strs[0] == None:
                return ""
            return strs[0]
        temp = ""
        for i in range(1, len(strs[0])+1):
            temp = strs[0][0:i]
            for j in strs:
                if strs[0][0:i] != j[0:i]:
                    return j[0:i-1]

        return temp
strs = ["",""]
s = Solution()
print(s.longestCommonPrefix(strs))
