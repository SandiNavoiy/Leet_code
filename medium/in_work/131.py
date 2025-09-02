class Solution:
    def partition(self, s: str) -> list[list[str]]:
        '''Палиндромная разбивка'''

        list = []

        if len(s)==1:
            return [[s[0]]]
        i=0

        while i < len(s):
            temp = []
            for j in range(len(s)):
                if s[j:i+j] == s[j:i+j][::-1]:
                    if len(s[j:i+j]) > 0:
                        temp.append(s[j:i+j])
                else:
                    continue
            if len(temp) > 0:
                list.append(temp)
            i+=1

        return list

s = Solution()
print(s.partition("a"))
# [["a","a","b"],["aa","b"]]