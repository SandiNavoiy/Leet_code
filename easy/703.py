class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.new = [k, nums]

    def add(self, val: int) -> int:
        self.new[1].append(val)
        self.new[1].sort(reverse=True)
        return self.new[1][self.new[0] - 1]


k = 3
nums = [4, 5, 8, 2]
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
print(obj.new)
val = 3
param_1 = obj.add(val)
print(obj.new)
print(param_1)
