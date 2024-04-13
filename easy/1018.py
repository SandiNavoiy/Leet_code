class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ''''''

        temp = str(nums[0])
        new = [int(temp, 2) % 5 == 0]
        for i in range(1,len(nums)):
            temp = temp + str(nums[i])

            new.append(int(temp,2) % 5 == 0)
        return new



nums = [0,1,1]
s = Solution()
print(s.prefixesDivBy5(nums))