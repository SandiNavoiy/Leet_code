class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """"""
        new = 0
        for i in nums:
            if i + diff in nums and i + 2 * diff in nums:
                new += 1

        return new


nums = [0, 1, 4, 6, 7, 10]
diff = 3
s = Solution()
print(s.arithmeticTriplets(nums, diff))
