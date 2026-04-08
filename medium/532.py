from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """"""
        nums.sort()
        print(nums)
        rez = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == k and (nums[i], nums[j]) not in rez:
                    rez.append((nums[i], nums[j]))
                    break



        return len(rez)



s = Solution()
print(s.findPairs([3, 1, 4, 1, 5], 2))
