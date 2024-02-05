class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        """"""
        nums.sort()
        x = 0
        for i in range(k):
            x = x + nums[-1]
            nums[-1] = nums[-1] + 1

        return x


nums = [
    4,
    4,
    9,
    10,
    10,
    9,
    3,
    8,
    4,
    2,
    5,
    3,
    8,
    6,
    1,
    10,
    4,
    5,
    3,
    2,
    3,
    9,
    5,
    7,
    10,
    4,
    9,
    10,
    1,
    10,
    4,
]
k = 6
s = Solution()
print(s.maximizeSum(nums, k))
