class Solution:
    def checkArithmeticSubarrays(
        self, nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        """"""
        rez = []
        for i in range(len(l)):
            temp = nums[l[i] : r[i] + 1]
            temp.sort()
            count = True
            for j in range(len(temp) - 1):
                if temp[j + 1] != temp[j] + (temp[1] - temp[0]):
                    count = False
            rez.append(count)
        return rez


nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]
s = Solution()
print(s.checkArithmeticSubarrays(nums, l, r))
