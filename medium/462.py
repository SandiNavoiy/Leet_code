class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        """"""
        rez = 0
        nums.sort()
        mediana = nums[len(nums) // 2]
        for i in nums:
            if i == mediana:
                continue
            rez = rez + abs(mediana - i)

        return rez


nums = [1, 10, 2, 9]
s = Solution()
print(s.minMoves2(nums))
