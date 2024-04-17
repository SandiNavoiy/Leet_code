class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """"""
        nums = nums[::-1]
        new = []
        iter = 0
        for i in nums:
            if i not in new and i <= k:
                new.append(i)
            iter += 1
            if len(new) == k:
                break
        return iter


nums = [3, 1, 5, 4, 2]
k = 2
s = Solution()
print(s.minOperations(nums, k))
