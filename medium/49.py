import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped_anagrams = collections.defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            print(sorted_s)
            grouped_anagrams[sorted_s].append(s)
        return list(grouped_anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))
