class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right+1])

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
left = 0
right = 2
obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
print(param_1)