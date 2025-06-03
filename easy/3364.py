class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        """"""

        ss = 10000000000000
        flag = False

        for i in range(len(nums)):
            for j in range(l, r + 1):
                if sum(nums[i : i + j]) > 0 and len(nums[i : i + j]) >= l:
                    ss = min(ss, sum(nums[i : i + j]))
                    flag = True

        if flag == False:
            return -1
        return ss


nn = [-2, 2, -3, 1]
l = 2
r = 3

s = Solution()
print(s.minimumSumSubarray(nn, l, r))
