class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        ''''''

        count = 0
        rez = nums[:3]
        if rez[0] + rez[2] == rez[1] / 2:
            count += 1

        for i in range(3, len(nums)):

            rez.pop(0)
            rez.append(nums[i])
            if rez[0] + rez[2] == rez[1] / 2:
                count += 1
        return count


s = Solution()
print(s.countSubarrays([1,2,1,4,1]))  # Output: 10
