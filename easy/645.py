class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """"""
        new = []
        for i in nums:
            if nums.count(i) == 2:
                new.append(i)
                if i - 1 not in nums:
                    if i - 1 == 0:
                        new.append(i + 1)
                    else:
                        new.append(i - 1)
                elif i + 1 not in nums:
                    new.append(i + 1)
                break

        return new


nums = [1, 1]
s = Solution()
print(s.findErrorNums(nums))
