class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """"""
        x = blocks.count("W")

        for i in range(len(blocks) - k + 1):
            print(blocks[i : i + k])
            if blocks[i : i + k].count("W") < x:
                x = blocks[i : i + k].count("W")
        return x


blocks = "WWBBBWBBBBBWWBWWWB"
k = 16
s = Solution()
print(s.minimumRecolors(blocks, k))
