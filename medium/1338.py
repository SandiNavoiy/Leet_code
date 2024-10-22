from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        """"""
        x = dict(Counter(arr))
        slov = sorted(x.items(), key=lambda x: x[1], reverse=True)
        rez = []
        sums = 0
        for i, j in slov:
            rez.append(i)
            sums = sums + j
            if sums >= len(arr) // 2:
                break

        return len(rez)

        return slov


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
s = Solution()
print(s.minSetSize(arr))
