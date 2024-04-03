class Solution:
    def countLargestGroup(self, n: int) -> int:
        """"""
        vvv = {}
        for i in range(1, n + 1):
            ss = 0
            for j in str(i):
                ss = ss + int(j)
            if ss not in vvv:
                vvv[ss] = [i]
            else:
                vvv[ss].append(i)
        sorted_dict = dict(
            sorted(vvv.items(), key=lambda item: len(item[1]), reverse=True)
        )
        max_length = len(sorted_dict[list(sorted_dict.keys())[0]])
        count_max_length = sum(
            1 for value in sorted_dict.values() if len(value) == max_length
        )
        return count_max_length


n = 2
s = Solution()
print(s.countLargestGroup(n))
