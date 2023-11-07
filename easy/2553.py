class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        """Разделить цифры в массиве"""
        new_list = []
        for i in nums:
            x = str(i)
            for j in x:
                new_list.append(int(j))
        return new_list


nums = [13, 25, 83, 77]
s = Solution()
print(s.separateDigits(nums))
