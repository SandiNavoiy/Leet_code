class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        x = 0
        for i in zip(*strs):
            print(i)
            print(list(i))
            print(sorted(i))

            if list(i) != sorted(i):
                x += 1

        return x


strs = ["cba", "daf", "ghi"]
s = Solution()
print(s.minDeletionSize(strs))
