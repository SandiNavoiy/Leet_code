class Solution:
    def greatestLetter(self, s: str) -> str:
        ''''''
        d = list(s)
        d.sort(reverse=True)


        for i in d:
            if  i == i.upper() and i.lower() in d:
                return i
        return ""



s = "nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"
sol = Solution()
print(sol.greatestLetter(s))