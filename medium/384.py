from copy import deepcopy
import random


class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def reset(self) -> list[int]:
        return self.nums

    def shuffle(self) -> list[int]:
        x = deepcopy(self.nums)
        random.shuffle(x)
        return x

# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
