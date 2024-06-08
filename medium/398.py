class Solution:
    def __init__(self, nums: list[int]):
        self.d = {}
        self.x = {}
        for i, j in enumerate(nums):
            if j not in self.d:
                self.d[j] = [i]
                self.x[j] = 0
            else:
                self.d[j].append(i)

    def pick(self, target: int) -> int:
        if self.x[target] <= len(self.d[target]) - 1:
            rez = self.d[target][self.x[target]]
            self.x[target] = self.x[target] + 1
            return rez
        else:
            self.x[target] = 0
            return self.d[target][self.x[target]]


nums = [1, 2, 3, 3, 3]
# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
print(obj.d)
print(obj.x)

target = 3
param_1 = obj.pick(target)
print(param_1)
