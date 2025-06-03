from collections import Counter


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        """"""
        rez = []

        for i in range(len(nums) - k + 1):
            temp = []
            for i, j in zip(
                list(
                    dict(
                        sorted(
                            Counter(nums[i : i + k]).items(),
                            key=lambda x: (x[1], x[0]),
                            reverse=True,
                        )
                    ).keys()
                )[:x],
                list(
                    dict(
                        sorted(
                            Counter(nums[i : i + k]).items(),
                            key=lambda x: (x[1], x[0]),
                            reverse=True,
                        )
                    ).values()
                )[:x],
            ):
                temp.append(i * j)
            rez.append(sum(temp))

        return rez


nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2


s = Solution()
print(s.findXSum(nums, k, x))
