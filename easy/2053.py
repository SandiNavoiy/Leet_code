class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ''''''
        new = [i for i in arr if arr.count(i) == 1]

        if len(new) < k:
            return ""
        return new[k-1]
arr = ["a","b","a"]
k = 3
s = Solution()
print(s.kthDistinct(arr, k))