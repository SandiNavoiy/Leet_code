from collections import deque


class Solution:
    def check(self, nums: list[int]) -> bool:
        ''''''


        new_sort = sorted(nums)
        arr = deque(nums)
        for i in range(len(new_sort)):
            arr.rotate(1)
            if list(arr) == new_sort:
                return True
        return False


nums = [6,10,6]
s = Solution()
print(s.check(nums))