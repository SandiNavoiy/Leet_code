class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        sec = set(path[1] for path in paths)
        fir = set(path[0] for path in paths)

        ans = sec - fir
        return ans.pop()


paths = [
    ["qMTSlfgZlC", "ePvzZaqLXj"],
    ["xKhZXfuBeC", "TtnllZpKKg"],
    ["ePvzZaqLXj", "sxrvXFcqgG"],
    ["sxrvXFcqgG", "xKhZXfuBeC"],
    ["TtnllZpKKg", "OAxMijOZgW"],
]
s = Solution()
print(s.destCity(paths))
# "OAxMijOZgW"
