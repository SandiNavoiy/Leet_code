class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        nums.sort()
        return nums


nums = [2,5,1,3,4,7]
n = int(3)

m = Solution()
print(m.shuffle(nums, n))