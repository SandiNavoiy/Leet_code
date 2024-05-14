class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """"""
        ss = []
        new = []
        rez = []
        for i in range(len(strs)):
            if strs[i] not in ss:
                temp = [strs[i]]
                for j in range(len(strs)):
                    if set(strs[i]) == set(strs[j]) and i != j:
                        temp.append(strs[j])
                        ss.append(strs[j])
                new.append(temp)
        new.sort()
        return new


strs = ["", ""]
s = Solution()
print(s.groupAnagrams(strs))
