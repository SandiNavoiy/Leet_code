class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """количество цифр мельне чем текущаяя"""
        new_list = []
        for i in nums:
            col = 0
            for j in nums:
                if i != j and i > j:
                    col = col + 1
            new_list.append(col)
        return new_list


nums = [8, 1, 2, 2, 3]
s = Solution()
print(s.smallerNumbersThanCurrent(nums))
