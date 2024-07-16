class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        ''''''
        rez = []
        new_arr = nums + nums

        for i in range(len(nums)):
            for j in range(i+1, len(new_arr)):
                flag = 0
                if new_arr[j] > nums[i]:
                    flag = 1
                    rez.append(new_arr[j])
                    break
            if flag == 0:
                rez.append(-1)

        return rez

nums = [1,2,1]
s = Solution()
print(s.nextGreaterElements(nums))
#[2,-1,2]